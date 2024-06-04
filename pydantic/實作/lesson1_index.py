from pprint import pprint
import HUH_window.pydantic.實作.tools as tools

def main():
    try:
        all_data:dict[any] = tools.download_json()
    except Exception as error:
        print(error)
    else:
        data:list[dict] = tools.get_data(all_data)
        pprint(data)

if __name__ == '__main__':
    main()