from src.text import Text
import pygame


class Globals:


    # display (late init)
    display: pygame.Surface = None

    # keyboard
    keys: set[int] = set()

    # game status
    is_running = False
    num_generations: int = 0
    
    # generations
    generation: list[list[int]] = None
    next_generation: list[list[int]] = None

    # patterns
    pattern_id = 1

    # texts (late init)
    text_num_generation: Text = None
    text_pause_resume: Text = None
    text_reset: Text = None

