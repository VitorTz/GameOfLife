#include "constants.h"
#include "GameOfLife.h"


int main() {
	InitWindow(gl::SCREEN_W, gl::SCREEN_H, gl::WINDOW_TITLE);
	SetTargetFPS(gl::FPS);
	gl::GameOfLife gameoflife{};

	while (WindowShouldClose() == false) {
		if (IsKeyPressed(KEY_SPACE)) {
			gameoflife.pause();
		}
		else if (IsKeyPressed(KEY_R)) {
			gameoflife.reset();
		}
		else if (IsKeyPressed(KEY_E)) {
			gameoflife.random_grid();
		}
		else if (IsKeyPressed(KEY_UP)) {
			gameoflife.change_cell_size(1);
		}
		else if (IsKeyPressed(KEY_P)) {
			gameoflife.print();
		}
		else if (IsKeyPressed(KEY_DOWN)) {
			gameoflife.change_cell_size(-1);
		}
		gameoflife.update();
		BeginDrawing();
		ClearBackground(gl::BACKGROUND_COLOR);
		gameoflife.draw();
		DrawFPS(20, 20);
		EndDrawing();
	}

	CloseWindow();
	return 0;
}