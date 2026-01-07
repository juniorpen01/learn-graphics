#version 330

in vec3 v_color;

out vec4 v_frag_color;

void main() {
    v_frag_color = vec4(v_color, 1);
}