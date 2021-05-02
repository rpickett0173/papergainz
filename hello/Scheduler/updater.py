from apscheduler.schedulers.background import BackgroundScheduler
from hello.views import GameData_Handler

def start():
    print("Started")
    scheduler = BackgroundScheduler()
    gamedata = GameData_Handler()
    # scheduler.add_job(gamedata.DotaRank,"interval", minutes=1, id="game_collector_001", replace_existing=True)
    scheduler.add_job(gamedata.get_api_data,"cron",hour=17,minute=46,second=00, id="API_job", replace_existing=True)
    # scheduler.add_job(gamedata.get_api_data,"interval", minutes=1, id="API_job", replace_existing=True)
    #scheduler.add_job(gamedata.calculate_payout_esport,"cron",hour=16 ,minute=49,second=30, id="Payout_job", replace_existing=True)
    # scheduler.add_job(gamedata.calculate_payout_sport,"cron",hour=17 ,minute=36,second=30, id="Payout_job", replace_existing=True)

    scheduler.start()
