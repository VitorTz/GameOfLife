#pragma once
#include <raylib.h>


#define SCREENSHOOT_DIR "./screenshots/"


namespace gl {


	// Window
	constexpr int SCREEN_W{ 1080 };
	constexpr int SCREEN_H{ 720 };
	constexpr Color BACKGROUND_COLOR{ 18, 18, 18, 255 };
	constexpr int FPS{ 120 };
	constexpr char WINDOW_TITLE[]{ "Game of Life" };

	// Grid
	constexpr int CELL_SIZE{ 20 };
	constexpr int GRID_ROWS{ SCREEN_H / CELL_SIZE };
	constexpr int GRID_COLS{ SCREEN_W / CELL_SIZE };
	constexpr int GRID_SIZE{ GRID_ROWS * GRID_COLS };
	constexpr int GRID_MIN_CELL_SIZE{ 1 };
	constexpr int GRID_MAX_CELL_SIZE{ 140 };
	constexpr int GRID_MAX_SIZE{ SCREEN_H / GRID_MIN_CELL_SIZE * SCREEN_W / GRID_MIN_CELL_SIZE };
	constexpr Color CELL_COLOR{ LIME };
}