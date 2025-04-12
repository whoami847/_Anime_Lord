from telegram.ext import Updater
from config import BOT_TOKEN
from handlers import setup_handlers
from plugins.forcesub import setup_forcesub
from plugins.file_saver import setup_file_saver
from plugins.batch_save import setup_batch_save
from plugins.auto_delete import setup_auto_delete
from plugins.copyright_warning import setup_copyright_warning
from plugins.user_settings import setup_user_settings
from plugins.custom_welcome import setup_custom_welcome
from plugins.broadcast import setup_broadcast
from plugins.font_style import setup_font_style
from plugins.copyright_message import setup_copyright_message

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    setup_handlers(dp)
    setup_forcesub(dp)
    setup_file_saver(dp)
    setup_batch_save(dp)
    setup_auto_delete(dp)
    setup_copyright_warning(dp)
    setup_user_settings(dp)
    setup_custom_welcome(dp)
    setup_broadcast(dp)
    setup_font_style(dp)
    setup_copyright_message(dp)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    import threading
    from http.server import HTTPServer, BaseHTTPRequestHandler

    class HealthCheckHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/health':
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'OK')
            else:
                self.send_response(404)
                self.end_headers()

    def run_health_check_server():
        server_address = ('', 8080)
        httpd = HTTPServer(server_address, HealthCheckHandler)
        httpd.serve_forever()

    threading.Thread(target=run_health_check_server, daemon=True).start()
    main()
