import logging


def shared_queue(task_to_queue):
    pass


def queue_task(condition, input_list):
    logging.debug('Starting queue_task...')

    with condition:
        for item in input_list:
            shared_queue.put(item)
        logging.debug(
            'Notifying fibonacci_task threads that'
            'the queue is ready to consume...'
        )
        condition.notify_all()
