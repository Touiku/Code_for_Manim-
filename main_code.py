import os
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from manim_voiceover.translate import get_gettext

# It is good practice to get the LOCALE and DOMAIN from environment variables
LOCALE = os.getenv("LOCALE")
DOMAIN = os.getenv("DOMAIN")

# The following function uses LOCALE and DOMAIN to set the language, and
# returns a gettext function that is used to insert translations.
_ = get_gettext()
pic="D:\\desktop\\phD aplli\ncsu\\output"
    

class I(VoiceoverScene,MovingCameraScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-GB-RyanNeural",
                style="newscast-casual",
                global_speed=1
            )
        )

        caption = Tex("Achilles and the Tortoise", font_size=72)
        name = Tex(r"$\Delta$ongyu $\Upsilon$ang", font_size=64)
        caption.next_to(name, UP, aligned_edge=DOWN, buff=2)
        rect = SurroundingRectangle(caption, buff=0.6, color=WHITE)
        self.add_sound("Zeta.mp3", gain=0.5)
        self.play(Write(caption),Create(rect),Write(name))
        self.wait(0.5)
        # Play the scene
        self.play(Uncreate(rect),Unwrite(caption),Unwrite(name))

        icon1=SVGMobject(f"archilles.svg",height=3.2,width=2.7)
        icon2=SVGMobject(f"tortoise.svg",height=3.2,width=2.7)
        icon1.to_edge(UP)
        icon2.next_to(icon1,RIGHT,buff=1)
        with self.voiceover(text="""Achilles is a god known for his running abilities in ancient Greek mythology, 
                            and now he is going to compete with the tortoise on the same track.""") as tracker:
            self.play(DrawBorderThenFill(icon1),DrawBorderThenFill(icon2),
                      run_time=tracker.duration)
        t1 = MathTable(
            [[0,1],
            ["\\frac{1}{2}","\\frac{1}{2}"]],
            row_labels=[
                Tex(r"Starting Point/$m$"),
                Tex(r"Velosity/$m\cdot s^{-1}$"),],
            col_labels=[Tex(r"Achilles($\alpha$)",color=BLUE), 
                            Tex(r"Tortoise($\tau$)",color=YELLOW)],
            h_buff=0.8)
        t1.to_edge(DOWN).align_to(DOWN)
        with self.voiceover(text="""Let's assume that the tortoise starts half a meter ahead of Achilles, but Achilles' speed is one meter per second, 
                            while the tortoise's speed is only half a meter per second.""") as tracker1:
            self.play(Write(t1),
                      run_time=tracker1.duration)
        upper_numberline = NumberLine(x_range=[0, 1.25, 0.25],
                                       include_numbers=True, 
                                       length=10, 
                                       numbers_to_exclude=[0.25],
                                       color=BLUE,
                                       decimal_number_config={"num_decimal_places": 2},
                                       include_tip=True)
        lower_numberline = NumberLine(x_range=[0, 1.25, 0.25], 
                                      include_numbers=True, 
                                      length=10, 
                                      numbers_to_exclude=[0.25,0.50,0.75,1],
                                      color=YELLOW,
                                        decimal_number_config={"num_decimal_places": 2},
                                      include_tip=True)
        lower_numberline.next_to(t1, UP)
        upper_numberline.next_to(lower_numberline, UP)

        alphadot = Dot(upper_numberline.n2p(0), color=WHITE)
        taudot = Dot(lower_numberline.n2p(0.5), color=WHITE)
        alpha = MathTex(r"\alpha").next_to(alphadot, UP, buff=0.3)
        tau = MathTex(r"\tau").next_to(taudot, DOWN, buff=0.3)

        with self.voiceover(text="""Now let's mark their positions on the coordinate axis. The blue color represents Achilles,
                             and the yellow color represents the turtle.""") as tracker2:
            self.play(ReplacementTransform(icon1,upper_numberline),
                    ReplacementTransform(icon2,lower_numberline),
                    Write(alpha),
                    Write(tau),
                    Create(alphadot),
                    Create(taudot),
                    run_time=tracker2.duration)
        f1= MathTex(r"\frac{1}{2}+\frac{t}{2}=t")
        f2=MathTex(r"\Downarrow")
        f2.next_to(f1,DOWN,buff=0.8)

        self.play(ReplacementTransform(t1,f1))
        self.play(Write(f2))

        f3= MathTex(r"t=1")
        f3.next_to(f2,DOWN,buff=0.8)
        self.play(Write(f3))

        n1=upper_numberline.n2p(1)
        n2=lower_numberline.n2p(1)
        
        def update_alpha(alpha):
            alpha.next_to(alphadot, UP, buff=0.3)
        def update_tau(tau):
            tau.next_to(taudot, DOWN, buff=0.3)

        with self.voiceover(text="""By separately writing out their equations of motion, 
                            we can solve for the moment when Achilles and the turtle meet, 
                            which is 1 second.""") :
            self.play(MoveAlongPath(alphadot,
                                 Line(alphadot.get_center(), n1), 
                                 run_time=3, rate_func=linear, 
                                 update_function=update_alpha),
                                 MoveAlongPath(taudot,
                                 Line(taudot.get_center(), n2), 
                                 run_time=3, rate_func=linear, 
                                 update_function=update_tau))

        alpha1 = MathTex(r"\alpha'").next_to(alphadot, UP, buff=0.3)
        tau1 = MathTex(r"\tau'").next_to(taudot, DOWN, buff=0.3)
        self.play(Unwrite(alpha),Unwrite(tau),Write(alpha1),Write(tau1))


        self.play(Unwrite(f1),
            FadeOut(f2,f3))

        self.play(FadeOut(upper_numberline, shift=UP),
            FadeOut(lower_numberline, shift=DOWN),
            FadeOut(alpha1, scale=0.5),
            FadeOut(tau1, scale=0.5),
            FadeOut(alphadot, scale=0.5),
            FadeOut(taudot, scale=0.5))
        
        icon3=SVGMobject(f"zeno.svg",height=3.2,width=2.7)
        icon3.to_edge(RIGHT)
        with self.voiceover(text="""However, Zeno offered a unique insight into this seemingly simple problem.
                            He argued that""") as tracker4:
            self.play(DrawBorderThenFill(icon3),
                    run_time=tracker4.duration)
        quote1=Tex(r"\textit{Achilles will never overpass the tortoise,}"  ,
                  )
        quote2=Tex(r"\textit{if the process is viewed from different  }","STEPS")
        quote2.set_color_by_tex('STEPS', RED)
        quote=VGroup(quote1,quote2).arrange(DOWN).next_to(icon3,LEFT,buff=0.4)
        with self.voiceover(text="""Achilles will never overpass the tortoise,
                             if the process is viewed from different STEPS.""") as tracker5:
            self.play(Write(quote),
                    run_time=tracker5.duration)

        self.play(FadeOut(icon3,quote))

        q1=Tex(r"\textit{Denote that:}")
        q1.to_edge(UP).align_to(UP)
        with self.voiceover(text="If we denote that:") as tracker6:
            self.play(Write(q1),run_time=tracker6.duration)

        
        q2=Tex(r"$x_{\alpha}$: the position of Achilles",color=BLUE).next_to(q1,DOWN)
        with self.voiceover(text="the position of Achilles is x alpha") as tracker7:
            self.play(Write(q2),run_time=tracker7.duration)
        q3=Tex(r"$v_{\alpha}$: the speed of Achilles",color=BLUE).next_to(q2,DOWN)
        with self.voiceover(text="the speed of Achilles is v alpha") as tracker8:
            self.play(Write(q3),run_time=tracker8.duration)
        q4=Tex(r"$x_{\tau}$: the position of the tortoise",color=YELLOW).next_to(q3,DOWN)
        with self.voiceover(text="the position of the tortoise is x tau") as tracker9:
            self.play(Write(q4),run_time=tracker9.duration)
        q5=Tex(r"$v_{\tau}$: the speed of the tortoise",color=YELLOW).next_to(q4,DOWN)
        with self.voiceover(text="the speed of the tortoise is v tau") as tracker10:
            self.play(Write(q5),run_time=tracker10.duration)

        t2 = MathTable(
            [["\\frac{1}{2}","\\frac{3}{4}",1,"\\frac{1}{2}","\\frac{1}{4}"]],
            row_labels=[
                Tex(r"\textsc{Step1}",color=RED)],
            col_labels=[Tex(r"$x_{\alpha}$",color=BLUE), Tex(r"$x_{\tau}$",color=YELLOW),Tex(r"$v_{\alpha}$",color=BLUE),
                            Tex(r"$v_{\tau}$",color=YELLOW),Tex(r"$x_{\tau}-x_{\alpha}$")],
            h_buff=0.8)
        t2.next_to(q5,DOWN)
        with self.voiceover(text="""In the first step, assuming the turtle has walked a quarter of the distance and reached three-quarters of the way, 
                            as Achilles' speed is twice that of the turtle, 
                            Achilles will reach the halfway point. 
                            At this moment, 
                            they will be a quarter of the distance apart.""") as tracker11:
            self.play(Write(t2),run_time=tracker11.duration)
        self.play(t2.animate.move_to(self.camera.frame_center),FadeOut(VGroup(q1,q2,q3,q4,q5)))

        t3 = MathTable(
            [["\\frac{3}{4}","\\frac{7}{8}",1,"\\frac{1}{2}","\\frac{1}{8}"]],
            row_labels=[
                Tex(r"\textsc{Step2}",color=RED)],
            col_labels=[Tex(r"$x_{\alpha}$",color=BLUE), Tex(r"$x_{\tau}$",color=YELLOW),Tex(r"$v_{\alpha}$",color=BLUE),
                            Tex(r"$v_{\tau}$",color=YELLOW),Tex(r"$x_{\tau}-x_{\alpha}$")],
            h_buff=0.8)
        with self.voiceover(text="""Using a similar method, we can calculate that in the second step, 
                            the distance between Achilles and the tortoise will 
                            shrink to one-eighth of the original distance.""") as tracker12:
            self.play(ReplacementTransform(t2,t3),run_time=tracker12.duration)

        t4 = MathTable(
            [["\\frac{7}{8}","\\frac{15}{16}",1,"\\frac{1}{2}","\\frac{1}{16}"]],
            row_labels=[
                Tex(r"\textsc{Step3}",color=RED)],
            col_labels=[Tex(r"$x_{\alpha}$",color=BLUE), Tex(r"$x_{\tau}$",color=YELLOW),Tex(r"$v_{\alpha}$",color=BLUE),
                            Tex(r"$v_{\tau}$",color=YELLOW),Tex(r"$x_{\tau}-x_{\alpha}$")],
            h_buff=0.8)
        with self.voiceover(text="""This goes similar with step three,""") as tracker13:
            self.play(ReplacementTransform(t3,t4),run_time=tracker13.duration)

        t5 = MathTable(
            [["\\frac{15}{16}","\\frac{31}{32}",1,"\\frac{1}{2}","\\frac{1}{32}"]],
            row_labels=[
                Tex(r"\textsc{Step4}",color=RED)],
            col_labels=[Tex(r"$x_{\alpha}$",color=BLUE), Tex(r"$x_{\tau}$",color=YELLOW),Tex(r"$v_{\alpha}$",color=BLUE),
                            Tex(r"$v_{\tau}$",color=YELLOW),Tex(r"$x_{\tau}-x_{\alpha}$")],
            h_buff=0.8)
        with self.voiceover(text="""step four,""") as tracker14:
            self.play(ReplacementTransform(t4,t5),run_time=tracker14.duration)

        tn = MathTable(
            [[r"1-\Big(\frac{1}{2}\Big)^n",r"1-\Big(\frac{1}{2}\Big)^{n+1}",1,r"\frac{1}{2}",r"\Big(\frac{1}{2}\Big)^{n+1}"]],
            row_labels=[
                Tex(r"\textsc{Step}  $n$",color=RED)],
            col_labels=[Tex(r"$x_{\alpha}$",color=BLUE), Tex(r"$x_{\tau}$",color=YELLOW),Tex(r"$v_{\alpha}$",color=BLUE),
                            Tex(r"$v_{\tau}$",color=YELLOW),Tex(r"$x_{\tau}-x_{\alpha}$")],
            h_buff=0.8)
        with self.voiceover(text="""and finally step n.""") as tracker15:
            self.play(ReplacementTransform(t5,tn),run_time=tracker15.duration)



        self.play(FadeOut(tn))
        numberline=NumberLine(x_range=[0, 1.25, 1/8],
                                       include_numbers=False, 
                                       length=12, 
                                       decimal_number_config={"num_decimal_places": 2},
                                       include_tip=True)
        label_1_2 = MathTex(r"\frac{1}{2}").next_to(numberline.n2p(1/2), DOWN)
        label_3_4 = MathTex(r"\frac{3}{4}").next_to(numberline.n2p(3/4), DOWN)
        label_1 = Tex(r"1").next_to(numberline.n2p(1), DOWN)
        label_0 = Tex(r"0").next_to(numberline.n2p(0), DOWN)
        a0=Tex(r"$\alpha$").next_to(numberline.n2p(0),UP)
        t0=Tex(r"$\tau$").next_to(numberline.n2p(1/2),UP)
        adot = Dot(numberline.n2p(0), color=BLUE)
        tdot = Dot(numberline.n2p(0.5), color=YELLOW)
        with self.voiceover(text="Represent this process on the coordinate axis.") :
            self.play(Create(numberline),Create(adot),Create(tdot),Write(label_0),Write(label_1),Write(label_1_2),Write(label_3_4),Write(a0),Write(t0))
        
        label_7_8=Tex(r"$\frac{7}{8}$").next_to(numberline.n2p(7/8), DOWN)
        label_15_16=Tex(r"$\frac{15}{16}$",font_size=27).next_to(numberline.n2p(15/16), DOWN)
        label_31_32=Tex(r"$\frac{31}{32}$",font_size=21).next_to(numberline.n2p(31/32), DOWN)
        label_63_64=Tex(r"$\frac{63}{64}$",font_size=13).next_to(numberline.n2p(63/64), DOWN)


        with self.voiceover(text="""It is not difficult to notice that as the number of steps increases, 
                                    the distance between the two becomes shorter and shorter. 
                                    However, Achilles can never catch up with the Tortoise within a finite number of steps. 
                                    """) :
            self.play(MoveAlongPath(adot,
                                 Line(adot.get_center(), numberline.n2p(1/2)), 
                                 run_time=2, rate_func=linear),
                                 MoveAlongPath(tdot,
                                 Line(tdot.get_center(), numberline.n2p(3/4)), 
                                 run_time=2, rate_func=linear),FadeOut(a0),FadeOut(t0),
                                 self.camera.frame.animate.scale(0.8).move_to(numberline.n2p(3/4)))
            self.wait(1.25)                     
        
            self.play(MoveAlongPath(adot,
                                 Line(adot.get_center(), numberline.n2p(3/4)), 
                                 run_time=2, rate_func=linear),
                                 MoveAlongPath(tdot,
                                 Line(tdot.get_center(), numberline.n2p(7/8)), 
                                 run_time=2, rate_func=linear),Write(label_7_8),
                                 self.camera.frame.animate.scale(0.8).move_to(numberline.n2p(7/8)))
            self.wait(1.25)

            self.play(MoveAlongPath(adot,
                                 Line(adot.get_center(), numberline.n2p(7/8)), 
                                 run_time=2, rate_func=linear),
                                 MoveAlongPath(tdot,
                                 Line(tdot.get_center(), numberline.n2p(15/16)), 
                                 run_time=2, rate_func=linear),Write(label_15_16),
                                 self.camera.frame.animate.scale(0.8).move_to(numberline.n2p(15/16)))
        
            self.wait(1.25)

            self.play(MoveAlongPath(adot,
                                 Line(adot.get_center(), numberline.n2p(15/16)), 
                                 run_time=2, rate_func=linear),
                                 MoveAlongPath(tdot,
                                 Line(tdot.get_center(), numberline.n2p(31/32)), 
                                 run_time=2, rate_func=linear),Write(label_31_32),
                                 self.camera.frame.animate.scale(0.8).move_to(numberline.n2p(31/32)))
            self.wait(1.25)

            self.play(MoveAlongPath(adot,
                                 Line(adot.get_center(), numberline.n2p(31/32)), 
                                 run_time=2, rate_func=linear),
                                 MoveAlongPath(tdot,
                                 Line(tdot.get_center(), numberline.n2p(63/64)), 
                                 run_time=2, rate_func=linear),Write(label_63_64),
                                 self.camera.frame.animate.scale(0.8).move_to(numberline.n2p(63/64)))
        
        
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14),FadeOut(numberline),
                    FadeOut(adot),FadeOut(tdot),FadeOut(label_0),FadeOut(label_1),FadeOut(label_1_2),
                    FadeOut(label_3_4),FadeOut(label_7_8),FadeOut(label_15_16),FadeOut(label_31_32),FadeOut(label_63_64))
        m0=MathTex(r"n\rightarrow\infty")
        with self.voiceover(text="So, only when n tends to infinity") as tracker16:
            self.play(Write(m0),run_time=tracker16.duration)
        m1=MathTex(r"\lim_{n\rightarrow\infty}x_{\tau}-x_{\alpha}=\lim_{n\rightarrow\infty}\Big(\frac{1}{2}\Big)^{n+1}=0").next_to(m0,DOWN)
        with self.voiceover(text="Achilles can \"truly\" catch up to the tortoise") as tracker17:
            self.play(Write(m1),run_time=tracker17.duration)

        m3=Tex(r"\textit{Why are they}").move_to(LEFT)
        m4=Tex(r"\textsc{Sooooo}", color=PINK).next_to(m3,RIGHT)
        m5=Tex(r"\textit{different}?").next_to(m4,RIGHT)
        with self.voiceover(text="""But why does the same physical process yield drastically
                             different outcomes when viewed from Zeno's perspective compared to the
                             normal angle of thinking?""") as tracker18:
            self.play(ReplacementTransform(VGroup(m0,m1),VGroup(m3,m4,m5)),run_time=tracker18.duration)
        self.play(Unwrite(VGroup(m3,m4,m5)))
        t6=MathTable(
            [[r"1",r"\frac{1}{2}"],
             [r"2",r"\frac{1}{2}+\frac{1}{4}"],
             [r"\cdots",r"\cdots"],
             [r"n",r"\sum_{k=1}^n\Big(\frac{1}{2}\Big)^k"]],
            col_labels=[Tex(r"$t'$ (Zeno's time)"),Tex(r" $t$ (Real-world time)")],
            h_buff=0.2)
        with self.voiceover(text="""
                            Now we will simultaneously depict the time (or calles steps) 
                            in the world of Zeno and the regular world on the same table.
                            In the first step in the world of Zeno, 
                            the real world has passed through 0.5 seconds.
                            Similarly, we can calculate that in the Zeno spacetime, 
                            after experiencing two steps, 
                            three steps, and up to n steps, 
                            the real world has elapsed for how long.""") as tracker18:
            self.play(Write(t6),run_time=tracker18.duration)

        self.play(FadeOut(t6))

        q6=Tex(r"$\ell$ : The original distance between them").next_to(q5,DOWN)
        group=VGroup(q5,q3,q6)
        rec=SurroundingRectangle(group, buff=0.6, color=PURPLE)
        with self.voiceover(text="Using the previously mentioned symbolic framework,") as tracker19:
            self.play(Write(group),Create(rec),VGroup(group,rec).animate.move_to(2*UP),run_time=tracker19.duration)

        m6=MathTex(r"t=\frac{\ell}{v_{\alpha}}\sum_{k=1}^n\Big(\frac{v_{\tau}}{v_{\alpha}}\Big)^k").next_to(VGroup(group,rec),DOWN)
        m7=MathTex(r"t=\frac{\ell}{v_{\alpha}-v_{\tau}}\bigg[1-\Big(\frac{v_{\tau}}{v_{\alpha}}\Big)^n\bigg]").next_to(VGroup(group,rec),DOWN)
        with self.voiceover(text="We can obtain the relationship between Zeno's time and regular time"):
            self.play(Write(m6))
            self.wait(2)
            self.play(ReplacementTransform(m6,m7))

        m8=MathTex(r"t'\rightarrow n").next_to(m7,UP)
        m9=MathTex(r"t=\frac{\ell}{v_{\alpha}-v_{\tau}}\bigg[1-\Big(\frac{v_{\tau}}{v_{\alpha}}\Big)^{t'}\bigg]").next_to(m8,DOWN)
        with self.voiceover(text="If we generalize the positive integer n to any real number t prime,") as tracker20:
            self.play(ReplacementTransform(VGroup(group,rec),m8),run_time=tracker20.duration)

        with self.voiceover(text="We can ultimately obtain the transformation of Zeno's spacetime.") as tracker21:
            self.play(ReplacementTransform(m7,m9),run_time=tracker21.duration)

        with self.voiceover(text="""Zeno's paradox prompted contemplation about the nature of the universe 
                            in the world of that time, 
                            leading people to question:""") as tracker22:
            self.play(FadeOut(VGroup(m8,m9)),run_time=tracker22.duration)

        q7=Tex(r"\textit{What is the essence of }\textsc{ time} ?").move_to(RIGHT)
        with self.voiceover(text="What is the essence of time?") as tracker23:
            self.play(Write(q7),run_time=tracker23.duration) 

        icon4=SVGMobject(f"galileo.svg",height=3.2,width=2.7).to_edge(LEFT)
        with self.voiceover(text="This question was not resolved until two thousand years later by an Italian named Galileo.") as tracker24:
            self.play(DrawBorderThenFill(icon4),run_time=tracker24.duration)   

        m10=MathTex(r"t'=t").move_to(UP)
        m11=MathTex(r"x'=x-vt").next_to(m10,DOWN)
        m12=MathTex(r"y'=y").next_to(m11,DOWN)
        m13=MathTex(r"z'=z").next_to(m12,DOWN)
        with self.voiceover(text="""This question was not resolved until two
                             thousand years later by an Italian named Galileo.
                            His classical view of spacetime considered time to flow uniformly, 
                            unaffected by the velocity of an object's motion. 
                            which effectively debunked the Zeno paradox.""") as tracker25:
            self.play(ReplacementTransform(q7,VGroup(m10,m11,m12,m13)),run_time=tracker25.duration)

        icon5=SVGMobject(f"einstein.svg",height=3.6,width=3.2).to_edge(LEFT)
        with self.voiceover(text="""However, the story doesn't end here. 
                            Four hundred years later, Albert Einstein introduced the 
                            theory of relativity and its spacetime concept.""") as tracker27:
            self.play(ReplacementTransform(icon4,icon5),FadeOut(VGroup(m10,m11,m12,m13)),
                      run_time=tracker27.duration)   
            

        m14=MathTex(r"t'=\frac{t-vx/c^2}{\sqrt{1-v^2/c^2}}").move_to(UP)
        m15=MathTex(r"x'=\frac{x-vt}{\sqrt{1-v^2/c^2}").next_to(m14,DOWN)
        m16=MathTex(r"y'=y").next_to(m15,DOWN)
        m17=MathTex(r"z'=z").next_to(m16,DOWN)
        with self.voiceover(text="""Although not in the form proposed by Zeno, 
                            he demonstrated that time and space are indeed closely interconnected.""") as tracker28:
            self.play(Write(VGroup(m14,m15,m16,m17)),run_time=tracker28.duration)

        icon3.to_edge(RIGHT)
        icon4=SVGMobject(f"galileo.svg",height=3.2,width=2.7)
        frame_center = self.camera.frame.get_center()
        icon4.move_to(frame_center)
        m18=MathTex("\Leftarrow").next_to(icon3,LEFT)
        m19=MathTex("\Leftarrow").next_to(icon4,LEFT)
        with self.voiceover(text="""From Zeno to Galileo and then to Einstein, 
                             the exploration of the essence of time by humanity has never ceased.
                             And isn't this the beauty of natural philosophy?""") as tracker29:
            self.wait(1)
            self.play(ReplacementTransform(VGroup(m14,m15,m16,m17),icon3),run_time=1.5)  
            self.wait(1)
            self.play(Write(m18))
            self.wait(0.5)
            self.play(SpiralIn(icon4),run_time=1.5)
            self.wait(1)
            self.play(Write(m19))
            self.wait(0.5)
            self.play(FadeOut(VGroup(icon3,m18,icon4,m19,icon5)))

            
        ti=Title(f"Credits")
        
        q8=Tex("Producer: Dongyu Yang").move_to(2*UP)
        q9=Tex("Music: Vincent Rubinetti").next_to(q8,DOWN)
        q10=Tex(r"Classical Machanics, Jiafu Cheng").next_to(q9,DOWN)
        q11=Tex(r"\texttt{https://docs.manim.community/en/stable}").next_to(q10,DOWN)
        q12=Tex(r"\texttt{https://www.wikiwand.com/en/Zeno}").next_to(q11,DOWN)


        self.play(FadeIn(VGroup(ti,q8,q9,q10,q11,q12)))
        self.wait(2.5)
        self.play(FadeOut(VGroup(ti,q8,q9,q10,q11,q12)))
