## Description of the principle of the lift:

This is a simple lift simulator. It is based on a finite state machine - [pytransitions](https://github.com/pytransitions)

#### The lift has the following conditions:
```
INIT_LIFT_POSITION_TRIGGER = 'INIT_LIFT_POSITION' - initial initialization of the lift position
GET_LIFT_TRIGGER = 'GET_LIFT' - call the lift to the floor
OPEN_LIFT_DOOR_TRIGGER = 'OPEN_LIFT_DOOR' - opening the lift door
CLOSE_LIFT_DOOR_TRIGGER = 'CLOSE_LIFT_DOOR' - closing the lift door
GO_TO_CHOSEN_FLOOR_TRIGGER = 'GO_TO_CHOSEN_FLOOR' - lift on an lift to the selected floor

```
### The principle of the lift
At the moment of the first start, the lift position is randomly selected between 'MIN_FLOOR_NUM' and entered 'floor_num'.

Then you need to enter your current location (floor).

To call the lift you need to use the following commands: START, start, Start, etc.

After entering this command, the lift will start moving in your direction.

After the lift arrives to your floor, the door opens, with the delay set.

Next you need to enter the floor number to which you need to climb. You can not enter a nonexistent floor or climb to the floor where you are now.

Example:
```bash
python run_lift.py --floor_num 10 --floor_height 2 --lift_speed 2 --door_time 1
``` 
### Safely lift stop
At any time, you can stop the lift by pressing CTRL + C. Depending on the current position of the lift, it will be safely stopped.

### Unit test
There are some unit tests in this repo.
run test
```bash
pytest -vv --cov=run_lift --cov-report term-missing tests/
```