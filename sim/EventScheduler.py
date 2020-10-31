class EventScheduler():
    def __init__(self):
        self.events = []
        self.c_moment = None
        self.c_position = None

    # TODO: Elaborar um método mais eficiente de enfileirar os eventos

    def addEvent(self, event):
        self.events.append(event)
        '''if len(self.events) == 0:
            self.events.append(event)
            self.c_moment = 0
            self.c_position = 0
        else:
            position = self.c_position
            for e in self.events[self.c_position:]:
                if event.getTime() < e.getTime():
                    self.events.insert(position, e)
                    self.c_position = position
                    return
                position += 1
            self.events.append(event)
            self.c_position = len(self.events) - 1'''

    def getEvents(self):
        return self.events

    def organize(self):
        self.events.sort(key=self.ascending)

    def ascending(self, event):
        return event.getTime()