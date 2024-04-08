import React, {useContext} from 'react'
import userContext from '../context/UserContext'

function profile() {
  const {user} = useContext(userContext)
 
    if (!user) return <div>Please Login</div>
    
    else if (user.username === "Harish") {
      return <div>Hello gandu {user.username}</div>
    }

    return <div>Welcome {user.username}</div>
   // return <div>Welcome {user.username}</div>
  
}

export default profile