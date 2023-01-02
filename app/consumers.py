
from channels.consumer import SyncConsumer,AsyncConsumer

class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })




class MySocket(SyncConsumer):
    def websocket_connect(self,event):
        self.send({
            'type':'websocket.accept'

        })


# class MySyncConsumer(SyncConsumer):

#     # def websocket_connect(self,event):
#     #     print("Web Socket Connect ",  event)
#     #     self.send({
#     #         'type':'websocket.accept'
#     #     })



#     def websocket_connect(self, event):
#         self.send({
#             "type": "websocket.accept",
#         })

#     def websocket_receive(self, event):
#         self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })



    # def websocket_receive(self,event):
    #     print("Web Socket receiver Start-  ", event)


    # def websocket_disconnect(self,event):
    #     print("Web Socket disconect  ",  event)




