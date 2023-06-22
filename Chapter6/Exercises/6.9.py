favorite_places = {
	"user1" : ["place1"],
	"user2" : ["place1","place2"],
	"user3" : ["place1","place2","place3"],
	"user4" : ["place1","place2","place3","place4"],
	"user5" : ["place5"],
}

for user,places in favorite_places.items():
	print(f"For {user}, places to visit are :")
	for place in places:
		print(f"\t{place}")
	print()