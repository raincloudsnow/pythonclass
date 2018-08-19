from sys import exit

def start():
    print("欢迎进入他的世界。")
    print("你出生在一个方块的世界里。")
    print("你看见许多的生物：羊、猪、牛、马、鸡，还有很多的树。")
    print("夜幕马上降临，你第一件事干什么？")
    print("1.杀羊，用羊毛做床，好好一觉到天亮。")
    print("2.砍树，做工作台，制作一把木剑，晚上去探险。")
    print("3.空手惨无人道地屠杀周围的一切生物。")

    door = input(">")
    if "1" in door:
        print("恭喜你！你安然度过了这个夜晚。你成功生存下来。")
        exit(0)
    
    elif "2" in door:
        adventure_room()
    
    elif "3" in door:
        food_room()
    
    else:
        start()


def adventure_room():
    print("黑夜里，你的眼前突然出现一只绿油油的僵尸，一只拿着弓箭的小白，一只囧字脸的苦力怕，一只高高瘦瘦的小黑。")
    print("你该怎么办？")
    print("1.二话不说，提着木剑冲上去，展开屠杀。")
    print("2.上前和他们友好的打招呼。")
    print("3.立马离开这个是非之地。")

    decision = input(">")
    if "1" in decision:
        dead("确实是屠杀，你被他们群殴至死。")
    
    elif "2" in decision:
        dead("苦力怕冒出白烟，只听砰的一声，大家都死翘翘了。")
    
    elif "3" in decision:
        print("你成功脱离了危险，迎来了第二天的太阳。")
        tommorow_room()
    
    else:
        print(f"好吧，{decision}应该更好些。")
        print("他们逃走了。")


def food_room():
    print("你杀死了周围的所有生物，得到了许多的食物：猪肉、牛肉、鸡肉。")
    print("但是你的残暴引来了这个世界除了你史蒂夫以外的另一个人Him。")
    print("Him对你的暴行感到十分的愤怒。")
    print("面对Him的愤怒，你该怎么办？")
    print("1.向他忏悔你的罪行，发誓做一个善良的人。")
    print("2.冲上去，管他什么Him不Him的，一个字：干！")

    choice = input(">")
    if "1" in choice:
        print("你得到了他的原谅，记住你的承诺。")
        print("你的真心使你胜利了！")
        exit(0)
    
    elif "2" in choice:
        dead("Him一言不发，把你打成了筛子。")
    
    else:
        food_room()

def tommorow_room():
    print("第二天的太阳升起了，你心中充满了对昨晚逃跑的庆幸。同时你对昨晚逃跑的行为感到憋屈。")
    print("于是你重新来到了昨晚遇见他们的地方。")
    print("只见小黑早已不见了踪影，小白和僵尸身上冒起了火焰，正在惨叫着，苦力怕却安然无恙，摆着亘古不变的囧字脸。")
    print("你该怎么办？")
    print("1.真是个好机会，拔剑冲上去，为昨晚的憋屈报仇。")
    print("2.不要一天打打杀杀，友好地上前，想要握手言和。")

    action = input(">")
    if "1" in action:
        print("你成功击杀了他们，得到了腐肉、骨头、火药，还有些经验。")
        print("你的英勇征服了他们，恭喜你！")
        exit(0)
    
    elif "2" in action:
        dead("苦力怕炸死了你！")

def dead(why):
    print(why,"干得漂亮!")
    exit(0)

start()