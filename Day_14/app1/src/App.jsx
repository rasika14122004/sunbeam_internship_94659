import { Navigate, Route, Routes } from "react-router"
import Home from "./pages/Home"
import Profile from "./pages/Profile"
import Login from "./pages/Login"
import Register from "./pages/Register"
import { ToastContainer } from 'react-toastify'
import { createContext, useState } from "react"

export const LoginContext = createContext()
// functional components
function App() {
  const [loginStatus, setLoginStatus] = useState(false)

  return (
    <>
      <LoginContext.Provider value={{ loginStatus, setLoginStatus }}>
        <Routes>
          <Route path="/*" element={<Login />} />
          <Route path="/register" element={<Register />} />
          {/* protecting the routes */}
          <Route path="/home" element={loginStatus ? <Home /> : <Navigate to='/' />} />
          <Route path="/profile" element={loginStatus ? <Profile /> : <Navigate to="/" />} />
        </Routes>
      </LoginContext.Provider>
      <ToastContainer />
    </>
  )
}

export default App
