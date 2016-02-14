#
#   This module creates a handler to deal with cisco Spark
#
#   notes
#   https://api.ciscospark.com/v1/rooms
import requests

SparkStatics = {
    'SPARK_URL': "https://api.ciscospark.com/v1/",
    'SPARK_TOKEN': 'Bearer OWJhYTM1ZTUtZGI3Ny00MjgyLWI0OGQtMDE2ZTAyNjhjNzI2YzIyNWIxNDEtMGMw'
}
SparkCodes = {
    204: "Room successfully deleted",
    200: "Action successfully commited"
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

    def _call_spark(self,what_to_do):
        pass

    def create_room(self):
        #   WORKING

        room = requests.post(SparkStatics['SPARK_URL']+"rooms",
                             headers={'Authorization': SparkStatics['SPARK_TOKEN'], 'content-type': 'application/json'},
                             json={'title': self._create_room_title()})
        room_id = room.json()
        #   WORKING
        return room_id['id']

    def delete_room(self, room_id):
        room = requests.delete(SparkStatics['SPARK_URL']+"rooms/"+room_id,
                               headers={'Authorization': SparkStatics['SPARK_TOKEN'], 'content-type': 'application/json'}
                               )
        return room.status_code

    # {
    #   "title" : bug_id
    #   }

psirt = {'ID': "CVE-2016-0021",
         'URI': "https://cisco.com/alles_ganz_doll_kaputt",
         'SYSTEM': 'Cisco ASA 55x5'
         }
# Testing Stuff
test = SparkInteraction(psirt)
spark_room = test.create_room()
print(spark_room)
status = test.delete_room(spark_room)
print(SparkCodes[status])
