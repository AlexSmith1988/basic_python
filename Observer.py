class Publisher:
    subscribers = []

    def __init__(self, *subscribers):
        [self.subscribe(subscriber) for subscriber in subscribers]

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def publish(self, x):
        [subscriber(x) for subscriber in self.subscribers]


publisher = Publisher(lambda x: print(f"new event: {x}"), lambda x: print(f"new event; {x * x}"))

[publisher.publish(x) for x in [1, 2, 3, 4, 5]]
