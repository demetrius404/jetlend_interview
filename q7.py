from typing_extensions import TypeAlias
from typing import Callable, List


Int: TypeAlias = int


def func(step: Int) -> None:
    print(f"step: {step}")


def create_handlers(callback: Callable) -> List[Callable]:
    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        #                      * lambda func definition fixed
        handlers.append(lambda s=step: callback(s))
        # handlers.append(lambda: callback(s))
    return handlers


def execute_handlers(handlers: List[Callable]) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()


if __name__ == "__main__":
    execute_handlers(create_handlers(func))
    # before        after
    # step: 4       step: 0
    # ...           ...
    # step: 4       step: 4

