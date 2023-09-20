![](https://github.com/renan-siqueira/FaceMoodMesh/blob/main/presentation.gif)

# FaceMoodMesh

This project is a tool developed in Python, which combines computer vision technologies to display videos with the capability to identify and annotate facial landmarks and emotions of faces present in the frames.

*__[Se você quer acessar a versão em Português, clique aqui](https://github.com/renan-siqueira/FaceMoodMesh-pt-BR)__*

---

## Why Choose FaceMoodMesh?

In an era where technology evolves swiftly, having tools that are both powerful and user-friendly is a true gem.

__"FaceMoodMesh"__ embodies this - striking a perfect balance between simplicity and efficacy.

If you're a beginner looking to delve into the captivating realm of computer vision, this is your ideal starting point.

For advanced users, it's a flexible platform that can be adapted and expanded according to your requirements.

The ability to visualize videos while simultaneously analyzing emotions and facial landmarks can be transformative in various fields, from entertainment to mental health.

Furthermore, with the modular nature of __"FaceMoodMesh"__, the sky's the limit when it comes to customization and extension.

Don't be misled by its straightforward setup and usage; beneath this accessible facade lies a robust tool, capable of offering valuable insights and in-depth analysis.

In essence, __"FaceMoodMesh"__ is the go-to combination for those aiming to achieve greatness without getting entangled in intricate setups and enigmatic code.

__Take the next step and discover for yourself!__

---

## Initial Setup

### 1. Virtual Environment Creation:

Firstly, it's highly recommended to use a virtual environment to isolate the project's dependencies.

```bash
$ python -m venv face_mood_mesh_env
```

__Activate the virtual environment:__

_On Windows:_
```bash
$ face_mood_mesh_env\Scripts\activate
```

_On Linux/Mac:_
```bash
$ source face_mood_mesh_env/bin/activate
```

---

### 2. Dependency Installation:

Within the virtual environment, install the required libraries:
```bash
$ pip install -r requirements.txt
```

---

### 3. Project Configuration:

3.1. Clone or download the project to your local machine:

    3.1.1 Open a terminal or command prompt on your computer.

    3.1.2 Navigate to the directory where you want to clone the project using the cd command. For instance:

    ```bash
    $ cd ~/Desktop
    ```

    3.1.3 Run the `git clone` command followed by the project's URL:

    ```bash
    $ git clone https://github.com/renan-siqueira/FaceMoodMesh.git
    ```

    3.1.4 Wait as Git clones the project on your computer. Once finished, you'll see a new folder named "FaceMoodMesh" in the chosen directory.

    3.1.5 Navigate to the cloned project's folder:

    ```bash
    $ cd FaceMoodMesh
    ```

    3.1.6 From here, you can proceed with installation and configuration steps as per the project documentation.

*__Remember: you need to have Git installed on your computer to execute these commands. If you haven't yet, you can download and install it from the [official Git website](https://git-scm.com/).__*

3.2. Rename the `settings.example.py` file to `settings.py`.

3.3. Update the variables in `settings.py`:

* `PATH_INPUT_DIR`: Specify the directory where your video is stored.

* `VIDEO_NAME`: Specify the video file name (including its extension).

* `PATH_MESSAGE_FILE`: By default, it's set as `messages.json`. Change only if you wish to use a different name.

* `PATH_EMOTION_TRANSLATION_FILE`: By default, it's `emotion_translation.json`. Modify if needed.

* `DISPLAY_WIDTH` e `DISPLAY_HEIGHT`: These are the display window sizes. Adjust according to your preference.

3.4. If you wish emotions to be translated into another language, adjust the `emotion_translation.json` file accordingly.

3.5. If new features are implemented or you wish to modify the shortcut keys, update the `messages.json` file to reflect these changes.

---

### 4. Running the Project:

After properly setting everything up, execute the `run.py` file:

```bash
$ python run.py
```

During its execution, you can:

Press `H` to display/hide the help menu.
Press `P` to pause/play the video.
Press `Q` to close the video.
Press `K` to show/hide facial landmarks.
Press `E` to show/hide emotions.

---

## Contributions and Contact

__FaceMoodMesh__ is an evolving project, and your contribution could be pivotal in making it even better!

If you have ideas, corrections, or new features you wish to add, feel free to open a pull request or file an issue.

If you have questions, suggestions, or want to discuss more about the project, contact me through my __[linkedin](https://www.linkedin.com/in/renan-siqueira-antonio-9b587054/)__!

I believe that, together, we can enhance and expand the capabilities of __FaceMoodMesh__, making it a benchmark in the field of computer vision.

*__Your feedback and expertise are invaluable to me.__*
