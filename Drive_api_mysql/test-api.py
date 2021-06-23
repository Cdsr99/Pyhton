
import gspread


gc = gspread.service_account(filename='/home/rodrigues/Downloads/service_account.json')
sh = gc.open_by_key('1EJ8HkA95IGD6MMGapRv6Hf4x0vTlJH-feb0AR4kmxyo')

print(sh.sheet1.get('a2'))
