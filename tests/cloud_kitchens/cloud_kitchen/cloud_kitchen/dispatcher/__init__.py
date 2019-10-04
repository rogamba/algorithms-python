from abc import ABCMeta


class Dispatcher(metaclass=ABCMeta):
    def dispatch(self, order_id: str):
        raise NotImplementedError()