import numpy as np
import pandas as pd
import time

np.random.seed(2) #reproducible
#1维世界的宽度,距离宝藏6步距离
N_STATES = 6 #the length of the 1 dimensional world
#探索者可用的动作:向左走or向右走？
ACTIONS = ['left','right']
#贪婪度:百分之90选择最优动作
EPSILON = 0.9 #greedy police
#学习率
ALPHA = 0.1 #learning rate
#未来奖励衰减值
GAMMA = 0.9 #discount factor
#最大回合数
MAX_EPISODES = 13 #maximum episodes
#移动间隔时间
FRESH_TIME = 0.3 #fresh time for one move

#建立Qtable
def build_q_table(n_states,actions):
    table = pd.DataFrame(np.zeros((n_states,len(actions))),#q_table initial values q_table全0初始
    columns = actions #action's name columns对应的是行为名称
    )
    # print(table)  #show table
    return table

#在某个state地点，选择行为
def choose_action(state,q_table):
    #选出这个state的所有action 值
    state_actions = q_table.iloc[state,:]
    if(np.random.uniform() > EPSILON ) or (state_actions.all() == 0):#非贪婪 or 或者这个state还没有探索过
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.argmax() #贪婪模式
    return action_name


def get_env_feedback(S,A):
    # This is how agent will interact with the environment
    if A == 'right': #move right
        if S == N_STATES - 2 : #terminate
            S_ = 'terminal'
            R = 1
        else: #move left
            S_ =S + 1
            R = 0
    else:
         R = 0
         if S == 0:
                S_ = S #reach the wall
         else:
                S_ = S - 1
    return S_,R

def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)

def rl():
    q_table = build_q_table(N_STATES,ACTIONS) #初始 q_table
    for episode in range(MAX_EPISODES): #回合
        step_counter = 0
        S = 0 #回合初始位置
        is_terminated = False #是否回合结束
        update_env(S,episode,step_counter) #环境更新
        while not is_terminated:
            A = choose_action(S,q_table) #选行为
            S_,R = get_env_feedback(S,A) #实施行为并得到环境的反馈
            q_predict = q_table.ix[S,A] #估算的(状态-行为)值
            if S_!='terminal':
                q_target = R + GAMMA * q_table.iloc[S_,:].max()
            else:
                q_target = R #实际的（状态-行为)值(回合结束)
                is_terminated = True #terminate this episode
            q_table.ix[S,A] +=ALPHA * (q_target - q_predict) #q_table更新
            S = S_ #探索者移动到下一个state
            update_env(S,episode,step_counter+1)#环境更新
            step_counter +=1

        return q_table

if __name__ == "__main__":
    q_table = rl()
    print("\r\nQ-table:\n")
    print(q_table)



