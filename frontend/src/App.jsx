import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import Dashboard from './pages/Dashboard'

function App() {
  // In future, replace this with real JWT auth check
  const isLoggedIn = true // Replace with actual auth logic

  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={isLoggedIn ? <Dashboard /> : <Navigate to="/login" />}
        />
        {/* You can add Login and Register routes later */}
        <Route path="*" element={<h1 className="text-white text-center mt-10">404 - Page Not Found</h1>} />
      </Routes>
    </Router>
  )
}

export default App
