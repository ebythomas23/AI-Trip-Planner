from utils.currency_convertor import CurrencyConverter
import os 
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class CurrencyConverterTool:
    def __init__(self) -> None:
        load_dotenv()
        self.api_key=os.environ.get("EXCHANGE_RATE_API_KEY")
        self.currency_service = CurrencyConverter(api_key=self.api_key)
        self.currency_converter_tool_list = self._setup_tools()

    def _setup_tools(self)->List:
        """ Setup tools for currency convertor tool"""

        @tool
        def convert_currency(amount:float, from_currency:str, to_currency:str):
            """ Conert amount from one currency to another"""
            return self.currency_service(amount, from_currency, to_currency)
        

        return [convert_currency]