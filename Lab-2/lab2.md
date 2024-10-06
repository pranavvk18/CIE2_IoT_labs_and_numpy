<!-- # ESP32 FreeRTOS Experiment -->
# Exp 1: Lab2_IoT_EC_exp1.ino

This experiment demonstrates the use of FreeRTOS on an ESP32 to run tasks on different cores. The ESP32's built-in LED is controlled, and multiple tasks are created and pinned to specific cores for concurrent execution.

### 1. Definitions and Initial Parameters
```cpp
#define LED_ESP32_BUILTIN 2
int param1 = 1000;
int param2 = 2000;
int param3 = 3000;
```

* `LED_ESP32_BUILTIN` is set to 2, which corresponds to the built-in LED on the ESP32.
* `param1`, `param2`, and `param3` are integer variables passed to tasks during their creation.

### 2. Setup Function

The `setup()` function is executed once when the board is powered on or reset.

```cpp
void setup() {
    pinMode(LED_ESP32_BUILTIN, OUTPUT);
    Serial.begin(115200);
    Serial.print("Setup: Executing on core ");
    Serial.println(xPortGetCoreID());
```

* The built-in LED is initialized as an output pin.
* The serial communication is started at a baud rate of 115200.
* The current core (Core 0 or Core 1) is printed to the serial monitor using `xPortGetCoreID()`.

### 3. Task Creation

Here, three tasks are created using FreeRTOS functions: `xTaskCreate()` and `xTaskCreatePinnedToCore()`.

```cpp
xTaskCreate(
    genericTask,
    "genericTask",
    10000,
    (void *)&param1,
    2,
    NULL);
delay(2000);
```

* **Task 1**: Created using `xTaskCreate()`, which runs on any available core.
* Task name: `"genericTask"`, and `param1` is passed to the task as a parameter.
* The priority of this task is set to 2.

```cpp
xTaskCreatePinnedToCore(
    genericTask,
    "Task_on_core0",
    10000,
    (void *)&param2,
    2,
    NULL,
    0);
delay(2000);
```

* **Task 2**: Created and pinned to **Core 0** using `xTaskCreatePinnedToCore()`.
* Task name: `"Task_on_core0"`, with `param2` as the parameter.

```cpp
xTaskCreatePinnedToCore(
    genericTask,
    "Task_on_core1",
    10000,
    (void *)&param3,
    2,
    NULL,
    1);
delay(2000);
```

* **Task 3**: Created and pinned to **Core 1**.
* Task name: `"Task_on_core1"`, with `param3` passed as the parameter.

### 4. Loop Function

The `loop()` function runs repeatedly and controls the LED's state.

```cpp
void loop() {
    Serial.printf("This loop() function is running on the core ID: %d\n", xPortGetCoreID());
    digitalWrite(LED_ESP32_BUILTIN, HIGH);
    delay(2000);
    digitalWrite(LED_ESP32_BUILTIN, LOW);
    delay(2000);
}
```

* Prints the core on which the loop is running.
* Toggles the LED on and off, with a delay of 2 seconds between each change.

### 5. Generic Task Function

The `genericTask()` function handles the behavior of the tasks created in the setup.

```cpp
void genericTask(void * parameter) {
    const char *taskName = pcTaskGetName(NULL);
    Serial.printf("Created the task: Executing genericTask() on the core %d\n", xPortGetCoreID());
    
    while(1) {
        delay(2000);
        Serial.printf("Task Name: %s\n", taskName);
        Serial.printf("This task genericTask() is running on the core %d\n", xPortGetCoreID());
        Serial.printf("Parameter passed to it on creation was %d\n", *(int*)parameter);
    }
}
```

* Retrieves the task name using `pcTaskGetName()`.
* The core on which the task is running is printed using `xPortGetCoreID()`.
* The task runs indefinitely, printing its name, the core it is running on, and the parameter passed during creation.

### Key Functions Used:

* `xTaskCreate()`: Creates a task that can run on any core.
* `xTaskCreatePinnedToCore()`: Creates a task and pins it to a specific core (Core 0 or Core 1).
* `xPortGetCoreID()`: Retrieves the core ID on which the current code is executing.

# Lab 2: my_printf() using the macros va_list, va_start, va_arg, va_end
* Macros are defined using the `#define` preprocessor directive, and as mentioned, they do not require a semicolon at the end.
*  Macros are simply textual replacements and do not allocate memory like variables do. Instead, wherever you use the macro in your code, the preprocessor replaces it with the value or code you define.

# C Variadic Functions: Key Macros Explained

## 1. `va_list`

* **What it does**: Declares a variable that will be used to store information about the additional arguments.
* **Syntax**:
```c
va_list argList;
```
* **How it works**:
   * This `va_list` variable is a special type that stores the information about the arguments passed to a variadic function (a function that accepts a variable number of arguments).
   * It doesn't hold the arguments themselves, but rather maintains information to access them.

## 2. `va_start`

* **What it does**: Initializes the `va_list` variable, so it knows where the list of additional arguments begins.
* **Syntax**:
```c
va_start(argList, lastFixedArg);
```
   * `argList`: This is the `va_list` variable that was declared.
   * `lastFixedArg`: This is the **last argument that is fixed** (not part of the variable arguments). You need to pass this so the compiler knows where to start looking for the variable arguments.
* **How it works**:
   * The `va_start()` macro sets up the `va_list` to start retrieving arguments right after the last fixed argument in the function.

**Example**:
```c
va_start(args, fmt);
```
Here, `fmt` is the last fixed argument, so `va_start()` will start looking for the next variable argument after `fmt`.

## 3. `va_arg`

* **What it does**: Retrieves the next argument from the list of variable arguments.
* **Syntax**:
```c
va_arg(argList, type);
```
   * `argList`: This is the `va_list` variable that was initialized by `va_start()`.
   * `type`: This is the type of the argument you want to retrieve (e.g., `int`, `char`, etc.).
* **How it works**:
   * `va_arg()` returns the **next argument** in the list of variable arguments and also moves to the next argument for future calls.
   * You have to know the type of each argument ahead of time (there's no automatic detection of the argument type).

**Example**:
```c
int param1 = va_arg(args, int);
```
This retrieves the next argument from the `args` list as an integer.

## 4. `va_end`

* **What it does**: Cleans up the `va_list` when you're done processing the arguments.
* **Syntax**:
```c
va_end(argList);
```
* **How it works**:
   * `va_end()` does any necessary cleanup (like freeing memory, depending on the implementation). It essentially closes the argument list.
   * It's good practice to call `va_end()` after you're done with your variable arguments.