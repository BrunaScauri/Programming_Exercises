from booking.booking import Booking

try:
  with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go('New York')
    bot.select_date(check_in_date="2022-10-20", 
    check_out_date="2022-10-25")
    bot.select_adults(10)
    bot.click_search()
    bot.apply_filtrations()
    # print(len(bot.report_results()))
except Exception as e:
  if 'in PATH' in str(e):
    print('There is a problem running the app from the command line.')
  else:
    raise


