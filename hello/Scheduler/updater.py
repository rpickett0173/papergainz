from apscheduler.schedulers.background import BackgroundScheduler
# from hello.views import GameData_Handler

def start():
    print("Started")
    scheduler = BackgroundScheduler()
    # gamedata = GameData_Handler()
    #scheduler.add_job(gamedata.DotaRank,"interval", minutes=1, id="game_collector_001", replace_existing=True)
    # scheduler.add_job(gamedata.get_api_data,"cron",hour=14 ,minute=23,second=30, id="API_job", replace_existing=True)
    #scheduler.add_job(gamedata.calculate_payout_esport,"cron",hour=23 ,minute=59,second=59, id="Payout_job", replace_existing=True)

    scheduler.start()
