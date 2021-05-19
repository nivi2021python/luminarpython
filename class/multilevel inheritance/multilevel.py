class Channels:
    def channel_category(self,language,type):
        self.language=language
        self.type=type
    def prnt_category(self):
        print(self.language)
        print(self.type)

class Channeltype(Channels):
    def type_of_channels(self,language,typesofinterest):
        self.language=language
        self.typesofinterest=typesofinterest
    def print_channeltypedetails(self):
        print(self.language)
        print(self.typesofinterest)
class Kids(Channeltype):
    def kids_channels(self,language,channel_name,channel_number):
        self.language=language
        self.channel_name=channel_name
        self.channel_number=channel_number
    def prnt_kidschannel(self):
        print(self.language)
        print(self.channel_number)
        print(self.channel_name)

kd=Kids()
ct=Channeltype()
ch=Channels()
kd.channel_category("malayalam","regional")
kd.prnt_category()
kd.type_of_channels("english","news")
kd.print_channeltypedetails()
kd.kids_channels("english","Pogo",206)
kd.prnt_kidschannel()