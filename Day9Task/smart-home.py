#Smart Home Devices (Multiple Inheritance) 
#A smart home device may have both WiFi connectivity and Voice control features. Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that inherits from both using multiple inheritance. 
class WiFiDevice:
    def connect_wifi(self):
        print("Device connected to WiFi")

class VoiceAssistant:
    def activate_voice(self):
        print("Voice assistant activated")

class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def play_music(self):
        print("Smart Speaker is playing music")

speaker = SmartSpeaker()

speaker.connect_wifi()
speaker.activate_voice()
speaker.play_music()