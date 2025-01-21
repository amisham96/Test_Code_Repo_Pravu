import azure.functions as func
import logging

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
                   use_monitor=False)
def zsdbi(myTimer: func.TimerRequest) -> None:

    try:
        logging.info('36 Python timer trigger function executed.')
        import zsbiconfig
        import sftplib
        # import triggerfunc

        if myTimer.past_due:
            logging.info('The timer is past due!')

        config = zsbiconfig.MyConfig(azure=True)
        print('config.ftp_host:', config.ftp_host)
        print('config.ftp_username:', config.ftp_username)
        print('config.ftp_password:', config.ftp_password)

        # err = triggerfunc.triggerfunc(config)

    except Exception as e:
        logging.exception(e)

    return
