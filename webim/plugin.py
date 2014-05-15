#!/usr/bin/env python
#coding: utf-8

"""
python webim plugin
"""

def webim_image(img):
    "static/webim/images/%s" % (img)

class Plugin:

    def __init__(self):
        """
        TODO:
        """
        pass

    def user(self):
        """
        Current user
        """
        return {
            'id': '1',
            'nick': 'user1',
            'presence': 'online',
            'show': "available",
            'pic_url': webim_image('male.png'),
            'url': "#",
            'role': 'user',
            'status':  ""
        }

    def buddies(self, uid):
        """
        Buddies of current uid

        Buddy:

        id:         uid
        uid:        uid
        nick:       nick
        pic_url:    url of photo
        presence:   online | offline
        show:       available | unavailable | away | busy | hidden
        url:        url of home page of buddy 
        status:     buddy status information
        group:      group of buddy

        """
        return [ {
            'id' => 'uid'+str(id),
            'group' => 'friend',
            'nick' => 'user'+str(id),
            'presence' => 'offline',
            'show' => 'unavailable',
            'status' => '#',
            'pic_url' => webim_image('male.png')
        } for id in range(1, 11) ]

        def buddies_by_ids(self, uid, ids):
            """
            Buddies by ids
            """
            return [{
                'id' => 'uid'+id,
                'group' => 'friend',
                'nick' => 'user'+id,
                'presence' => 'offline',
                'show' => 'unavailable',
                'status' => '#',
                'pic_url' => webim_image('male.png')
            } for id in ids ]

        def rooms(self, uid):
            """
            Rooms of current uid
            id:		    Room ID,
            nick:	    Room Nick
            url:	    Home page of room
            pic_url:    Pic of Room
            status:     Room status 
            count:      count of online members
            all_count:  count of all members
            blocked:    True | False
            """
            return [{
                'id': 'room1',
                'name': 'room1',
                'nick': 'Room',
                'url': "#",
                'pic_url': webim_image('room.png'),
                'status': "Room",
                'blocked': False,
                'temporary': False
            }]

    def rooms_by_ids(self, uid, ids):
        """
        Rooms by ids
        """
        return [ {
            'id':   $id,
            'name': $id,
            'nick': "Room",
            'url': "#",
            'pic_url': webim_image('room.png')
        } for id in ids if id == 'room1']

    def members(self, room):
        """
        Members of room
        """
        return [ {
            'id':   'uid' + str(id),
            'nick': 'user' + str(id)
        } for id in range(1, 11) ]

    def notifications(self, uid):
        """
        Notifications of current user

        Notification:
        
        text: text
        link: link
        """
        return []

    def menu(self, uid):
        """
        Menu of current user

        Menu:

        icon
        text
        link
        """
        return []

