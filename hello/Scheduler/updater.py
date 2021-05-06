from apscheduler.schedulers.background import BackgroundScheduler
from hello.views import GameData_Handler

def start():
    print("Started")
    scheduler = BackgroundScheduler()
    gamedata = GameData_Handler()
    # Cron timers
    # scheduler.add_job(gamedata.DotaRank,"cron",hour=4,minute=59,second=59, id="game_collector_001", replace_existing=True)
    # scheduler.add_job(gamedata.get_api_data,"cron",hour=4,minute=59,second=59, id="API_job", replace_existing=True)
    # scheduler.add_job(gamedata.calculate_payout_esport,"cron",hour=4 ,minute=59,second=59, id="Payout_job", replace_existing=True)
    # scheduler.add_job(gamedata.calculate_payout_sport,"cron",hour=4,minute=59,second=59, id="Payout_job", replace_existing=True)

    # interval timers
    scheduler.add_job(gamedata.DotaRank,"interval", minutes=5, seconds=0, id="game_collector_001", replace_existing=True)
    scheduler.add_job(gamedata.get_api_data,"interval", minutes=5, seconds=0, id="API_job", replace_existing=True)
    scheduler.add_job(gamedata.calculate_payout_esport,"interval", minutes=5, seconds=0, id="eSportPayout_job", replace_existing=True)
    scheduler.add_job(gamedata.calculate_payout_sport,"interval", minutes=5, seconds=0, id="SportPayout_job", replace_existing=True)

    # Force timers (UTC)
    # scheduler.add_job(gamedata.DotaRank, "cron",hour=0,minute=58,second=0, id="game_collector_001", replace_existing=True)
    # scheduler.add_job(gamedata.get_api_data, "cron",hour=0,minute=58,second=0, id="API_job", replace_existing=True)
    # scheduler.add_job(gamedata.calculate_payout_esport, "cron",hour=0,minute=58,second=0, id="eSportPayout_job", replace_existing=True)
    # scheduler.add_job(gamedata.calculate_payout_sport, "cron",hour=0,minute=58,second=0, id="SportPayout_job", replace_existing=True)

    scheduler.start()
