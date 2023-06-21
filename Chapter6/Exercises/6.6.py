favorite_languages = {
	"jen" : "python",
	"sarah" : "c",
	"edward" : "ruby",
	"phil" : "go",
}

names = ("jen", "edward", "user1", "user2")

for name in names:
	if name in favorite_languages.keys():
		print(f"{name.title()} thanks for taking the poll")
	else:
		print(f"{name.title()}, we invite you to take the poll")

