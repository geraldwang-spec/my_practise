

from stocks_project.stock_process import stock_process_module


def stock_init()->None:
    print(f"test stock_init")
    stock_p:stock_process_module = stock_process_module()
    stock_p.process_stocks_data()
