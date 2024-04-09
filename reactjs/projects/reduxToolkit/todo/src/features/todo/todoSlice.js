import {createSlice , nanoid} from "@reduxjs/toolkit"

const initialState = {
    todos : [{
        id : 1 , 
        text : "hello world" , 

    }]
}

export const TodoSlice = createSlice({
    name : "dishant" , 
    initialState , 
    reducers : {
        addTodo : (state , action ) => {
            const todo = {
                id: nanoid()   , 
                text : action.payload
            }
            state.todos.push(todo)
        } , 
        removeTodo : (state , action ) => {
                state.todos = state.todos.filter((todo) => todo.id !== action.payload)
        } ,
        updateTodo : (state , action ) => {
                state.todos = state.todos.filter((todo)=> todo.id === action.payload ? todo.text = action.text : todo)
        } 

        
        
    }
})
export const {addTodo , removeTodo , updateTodo} = TodoSlice.actions

export default TodoSlice.reducer
