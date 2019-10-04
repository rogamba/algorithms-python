from abc import ABCMeta


class DriverDispatcher(metaclass=ABCMeta):
    def dispatch(self, order_id: str):
        raise NotImplementedError()