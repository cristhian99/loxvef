# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image rip="rip.png"
image elvis="elvis.png"
image laser="laser.png"
image soy="soy.png"
image mundo="mundo.png"
image colada="colada.png"
image agent="agent.png"
image monstruo="monstruo.png"
image haha="haha.png"
image planeta="planeta.png"


# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define a= Character('Loxvef', color="#2E2EFE")
define b= Character('Agent Carter',color="#FF8000")

# The game starts here.
label start:
    play sound"mi nombre es loxvef.wav"
    show soy
    a"Mi nombre es Loxvef"
    show planeta
    play sound"mi planeta se llama resdel.wav"
    a"Mi planeta se llama Resdel"
    show monstruo
    play sound"fui criado para conquistar.wav"
    a"Fui criado para conquistar y esclavizar otras razas"
    show mundo
    play sound"y la tierra.wav"
    a"La tierra es la siguiente"
    show haha
    play sound"Hahaha.wav"
    a"HAHAHAHA"
    play sound"mas hahaha.wav"
    show haha at right
    a"MAS HAHAHAH"
    menu:
        "Conquistar la tierra":
            jump choice1_yes
        "No conquistar la tierra":
            jump choice1_no
            
    label choice1_yes:
        $menu_flag=True
    show agent
    play sound"lo que no sabia loxvef.wav"
    b"Lo que no sabia Loxvef, es que durante años hemos estado construyendo un misil anti aliens"
    show elvis
    play sound"lo empezamos a construir cuando.wav"
    b"Lo empezamos a construir cuando nos dimos cuenta que Elvis Presley era uno"
    jump choice1_doone
    
    label choice1_no:
        $menu_flag=False
        play sound"pos me quedo tomando.wav"
        show colada
    a"Pos me quedo tomando piñas coladas"
    return
    
    label choice1_doone:
    menu:
        "Disparar rayo":
            jump choice2_yes
        "No disparar rayo":
            jump choice2_no
            
    label choice2_yes:
        $menu_flag=True
    show laser
    play sound"no voy a mentirte.wav"
    b"No voy a mentir, esto primero va a dolerte y luego a pulverizarte"
    show rip
    "Pos esta muerto"
    return
        
    label choice2_no:
        $menu_flag=False
    show rip
    play sound"pos nos morimos.wav"
    b"Pos nos morimos"
    show haha
    play sound"hay los humanos.wav"
    a"Hay los humanos, siempre tan tontos"
            
        
    
        
 

    return
