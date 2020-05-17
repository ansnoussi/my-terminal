#!/bin/env python3
__header__='''
         \x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;39;48;43m▄\x1b[0m             
       \x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[38;2;39;48;43m▄\x1b[0m          
      \x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;39;48;43m▄\x1b[0m      
    \x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[38;2;39;48;43m▄\x1b[0m    
   \x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;221;163;56m▄\x1b[0m\x1b[38;2;39;48;43m▄\x1b[0m 
  \x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;39;48;43m▀\x1b[0m \x1b[38;2;64;130;241m     ██      ▄   ▄█    ▄▄▄▄▄          ▄▄▄▄▄    ▄  █ ████▄   ▄ ▄       █▀▄▀█ ▄███▄   \x1b[0m
 \x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m \x1b[38;2;64;130;241m     █ █      █  ██   █     ▀▄       █     ▀▄ █   █ █   █  █   █      █ █ █ █▀   ▀  \x1b[0m
 \x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m \x1b[38;2;64;130;241m     █▄▄█ ██   █ ██ ▄  ▀▀▀▀▄       ▄  ▀▀▀▀▄   ██▀▀█ █   █ █ ▄   █     █ ▄ █ ██▄▄    \x1b[0m
\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;245;235;226m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;64;130;241m     █  █ █ █  █ ▐█  ▀▄▄▄▄▀         ▀▄▄▄▄▀    █   █ ▀████ █  █  █     █   █ █▄   ▄▀ \x1b[0m
\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;245;235;226m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;64;130;241m        █ █  █ █  ▐                              █         █ █ █         █  ▀███▀   \x1b[0m
\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;64;130;241m       █  █   ██                                ▀           ▀ ▀         ▀           \x1b[0m
\x1b[38;2;39;48;43m▀\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m \x1b[38;2;64;130;241m      ▀                                                                             \x1b[0m
 \x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m \x1b[38;2;64;130;241m       ▄ ▄    ▄  █ ██     ▄▄▄▄▀     ▀▄    ▄ ████▄   ▄         ▄▀  ████▄    ▄▄▄▄▀    \x1b[0m
  \x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;39;48;43m▀\x1b[0m \x1b[38;2;64;130;241m      █   █  █   █ █ █ ▀▀▀ █          █  █  █   █    █      ▄▀    █   █ ▀▀▀ █       \x1b[0m
   \x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m  \x1b[38;2;64;130;241m     █ ▄   █ ██▀▀█ █▄▄█    █           ▀█   █   █ █   █     █ ▀▄  █   █     █       \x1b[0m
    \x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m   \x1b[38;2;64;130;241m     █  █  █ █   █ █  █   █            █    ▀████ █   █     █   █ ▀████    █        \x1b[0m
     \x1b[38;2;39;48;43m▀\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m    \x1b[38;2;64;130;241m      █ █ █     █     █  ▀           ▄▀           █▄ ▄█      ███          ▀         \x1b[0m
      \x1b[38;2;39;48;43m▀\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m     \x1b[38;2;64;130;241m       ▀ ▀     ▀     █                             ▀▀▀                              \x1b[0m
       \x1b[38;2;39;48;43m▀\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m     \x1b[38;2;64;130;241m                    ▀                                                               \x1b[0m
         \x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m     
          \x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;39;48;43m\x1b[38;2;39;48;43m▄\x1b[0m     
           \x1b[38;2;39;48;43m▀\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;39;48;43m▀\x1b[0m     
             \x1b[38;2;39;48;43m▀\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;248;198;77m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;248;198;77m\x1b[38;2;224;164;52m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;39;48;43m▀\x1b[0m      
               \x1b[38;2;39;48;43m▀\x1b[0m\x1b[38;2;39;48;43m▀\x1b[0m\x1b[38;2;39;48;43m▀\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[48;2;224;164;52m\x1b[38;2;39;48;43m▄\x1b[0m\x1b[38;2;39;48;43m▀\x1b[0m\x1b[38;2;39;48;43m▀\x1b[0m        
'''
print(__header__)                                                              
                                            