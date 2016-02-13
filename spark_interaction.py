#
#   This module creates a handler to deal with cisco Spark
#
#   notes
#   https://api.ciscospark.com/v1/rooms
import requests

SparkStatics = {
    'SPARK_URL': "https://api.ciscospark.com/v1/rooms",
    'SPARK_TOKEN': 'Bearer NmY2ODA5ZjUtOGQ1YS00MzJkLWEyYjctZDg2ZWMzN2IyNDYzOTgwOTg2OTctZGI3'
}


class SparkInteraction:
    def __init__(self, bug_notification):
        """
            Initializes SparkInteraction object
        Args:
            bug_notification: expects a dictionary with
                ID = Cisco Advisory ID of BUG
                URI    = BUG description URL
                SYSTEM = affected Systems
        """
        self.bug_notification = bug_notification
        pass

    def _create_room_title(self):
        """
            Generates a Room title to be setup in Spark
        Returns:
            final Room Title
        """
        room_title = "Spark Conference to address issue: " + self.bug_notification['ID']

        return room_title

    def create_room(self):
        #   WORKING
        room = requests.post(SparkStatics['SPARK_URL'],
                             headers={'Authorization': SparkStatics['SPARK_TOKEN'], 'content-type': 'application/json'},
                             json={'title': self._create_room_title()})
        room_data = room.json()
        #   WORKING
        return room_data['id']

    # {
    #   "title" : bug_id
    #   }

psirt = {'ID': "CVE-2016-0021",
         'URI': "https://cisco.com/alles_ganz_doll_kaputt",
         'SYSTEM': 'Cisco ASA 55x5'
         }
test = SparkInteraction(psirt)
spark_room = test.create_room()
print(spark_room)
