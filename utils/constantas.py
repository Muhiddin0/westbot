
import os
import dotenv

dotenv.load_dotenv()

COMMENT_SEND_ID = os.getenv('COMMENT_SEND_ID') # comment id
COMMENT_MESSAGE_THREAD_ID = os.getenv('COMMENT_MESSAGE_THREAD_ID') # comment thread id
ORDER_SEND_CHAT = os.getenv('ORDER_SEND_CHAT') # order id
ORDER_TAKE_MESSAGE_THREAD_ID = os.getenv('ORDER_TAKE_MESSAGE_THREAD_ID')
ORDER_DELIVERY_MESSAGE_THREAD_ID = os.getenv('ORDER_DELIVERY_MESSAGE_THREAD_ID')


KITCHEN_LAN = 40.7128
KITCHEN_LON = -74.0060