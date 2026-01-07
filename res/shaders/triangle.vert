#version 330

in vec2 a_pos;
in vec3 a_color;

out vec3 v_color;

void main() {
    v_color = a_color;
    gl_Position = vec4(a_pos, 0, 1); // NOTE: i forgor what z and w do in this case but prolly not that important with what i need
}