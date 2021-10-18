import threading
import random
import time
import uuid
import settings as settings



class DinningHall(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(DinningHall, self).__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(1)
            self.generate_random_order()

    @staticmethod
    def generate_random_order():
        (table_idx, table) = next(((i, table) for i, table in enumerate(settings.TABLES) if table['state'] == settings.TABLE_FREE), (None, None))
        if table_idx is not None:
            max_wait_time = 0
            items = []
            for i in range(random.randint(1, 5)):
                food = random.choice(settings.FOODS)
                if max_wait_time < food['preparation-time']:
                    max_wait_time = food['preparation-time']
                items.append(food['id'])
            max_wait_time = round(max_wait_time * 1.3)

            new_order_id = uuid.uuid4().hex
            new_order = {
                'id': new_order_id,
                'items': items,
                'priority': random.randint(1, 5),
                'max_wait': max_wait_time,
                'table_id': table['id']
            }
            settings.ORDER_Q.put(new_order)
            settings.ORDER_LIST.append(new_order)

            settings.TABLES[table_idx]['state'] = settings.TABLE_WAITING_FOR_WAITER
            settings.TABLES[table_idx]['order_id'] = new_order_id
        else:
            time.sleep(random.randint(2, 10) * settings.TIME_UNIT)
            idxs = [table for table in settings.TABLES if table['state'] == settings.TABLE_ORDER_SERVED]
            if len(idxs):
                rand_idx = random.randrange(len(idxs))
                settings.TABLES[rand_idx]['state'] = settings.TABLE_FREE