#
#   This module creates a handler to deal with cisco Spark
#
#   notes
#   https://api.ciscospark.com/v1/rooms
import requests
import DB_Data

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
        self.room_id = "Not Created"
        pass

    def __str__(self):
        return self.room_id

    def _create_room_title(self):
        """
            Generates a Room title to be setup in Spark
        Returns:
            final Room Title
        """
        room_title = self.bug_notification['ID']+" - Spark Conference"

        return room_title

    def create_room(self):
        #   WORKING

        room = requests.post(SparkStatics['SPARK_URL']+"rooms",
                             headers={'Authorization': SparkStatics['SPARK_TOKEN'], 'content-type': 'application/json'},
                             json={'title': self._create_room_title()})
        self.room_id = room.json()['id']

        #   WORKING

    # TODO: Clean delete room
    #def get_membership_in_room(self):
    #    members_list = requests.get(SparkStatics['SPARK_URL']+"memberships",
    #                                headers={'Authorization': SparkStatics['SPARK_TOKEN'],
    #                               '        content-type': 'application/json'},
    #                                json={}


    def delete_room(self):
        """
            removes a room from Spark with self.room_id
        Returns:
            Status Code of Room - if OK 204
        """
        room = requests.delete(SparkStatics['SPARK_URL']+"rooms/"+self.room_id,
                               headers={'Authorization': SparkStatics['SPARK_TOKEN'],
                                        'content-type': 'application/json'}
                               )
        return room.status_code

    def invite_users_to_room(self, user_id_list):
        for user_id in user_id_list:
            requests.post(SparkStatics['SPARK_URL']+"memberships",
                          headers={'Authorization': SparkStatics['SPARK_TOKEN'],
                                   'content-type': 'application/json'},
                          json={'roomId': self.room_id,
                                'personEmail': DB_Data.User_ID[user_id]['mail'],
                                'isModerator': False})


psirt = {'ID': "CVE-2016-0021",
         'URI': "https://cisco.com/alles_ganz_doll_kaputt",
         'SYSTEM': 'ASA'
         }
# Testing Stuff
test = SparkInteraction(psirt)
test.create_room()
print(test)

call_participants = DB_Data.Device_type[psirt['SYSTEM']]
test.invite_users_to_room(call_participants)
#   status = test.delete_room()
#   print(SparkCodes[status])
