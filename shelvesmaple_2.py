# This is an exapmle of updating data into a shelve
# anime name and its characters is saved in a shelve and then update
import shelve

DBZ = ["Goku","vegeta","gohan"]
oregairu = ["hachiman","yukino","yui"]
naruto = ["naruto","sasuke","sakura"]
eureka7 = ["eruka","holland","renton"]

with shelve.open("anime",writeback=True) as anime:
    anime["DBZ"] = DBZ
    anime["oregairu"] = oregairu
    anime["naruto"] = naruto
    anime["eureka7"] = eureka7

    for name in anime:
        print(" {}: are the characters of {} anime" .format(anime[name],name))
    print("-"*50)
    # anime["DBZ"].append("trunks")  - This will not update the database
   
    # temp = anime["DBZ"]
    # temp.append("trunks")
    # anime["DBZ"] = temp
    #       OR 
    # you can simply set writeback = True, when you are opening shelve
    anime["naruto"].append("kakashi")
    #anime.sync()  # If we use sync() the bellow code will not work as, sync() cleares the cache
    eureka7.append("tallho")
    for val in anime.values():
        print(val)

