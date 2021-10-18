import settings as settings
from clientService.DinningHall import DinningHall
from clientService.Waiter import Waiter
import logging
from flask import Flask, request
import threading

logging.basicConfig(filename='dinning.log', level=logging.DEBUG, format='%(asctime)s:  %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)

app = Flask(__name__)

threads = []

@app.route('/distribution', methods=['POST'])
def distribution():
    order = request.get_json()
    logger.info(f'NEW DISTRIBUTION orderId: {order["order_id"][0:4]}')

    table_idx = next((i for i, table in enumerate(settings.TABLES) if table['id'] == order['table_id']), None)
    settings.TABLES[table_idx]['state'] = settings.TABLE_WAITING_FOR_ORDER_TO_BE_SERVED

    waiter_thread: Waiter = next((w for w in threads if type(w) == Waiter and w.id == order['waiter_id']), None)
    waiter_thread.serve_order(order)
    return {'isSuccess': True}


def start_dinning():
    flask_thread = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False), daemon=True)
    threads.append(flask_thread)

    dh_thread = DinningHall()
    threads.append(dh_thread)

    for _, w in enumerate(settings.WAITERS):
        waiter_thread = Waiter(w)
        threads.append(waiter_thread)

    for th in threads:
        th.start()
    for th in threads:
        th.join()


if __name__ == '__main__':
    start_dinning()