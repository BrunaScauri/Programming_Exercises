from booking.booking import Booking

with Booking() as bot:
  bot.land_first_page()
  bot.change_currency(currency='USD')
  bot.select_place_to_go('New York')
  bot.select_date(check_in_date="2022-10-16", check_out_date="2022-10-23")