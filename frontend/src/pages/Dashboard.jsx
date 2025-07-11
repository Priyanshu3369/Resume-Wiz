import ResumeForm from "../components/ResumeForm"
import ResumePreview from "../components/ResumePreview"

export default function Dashboard() {
  return (
    <div className="grid grid-cols-2 gap-4 p-4 min-h-screen bg-black text-white">
      <ResumeForm />
      <ResumePreview />
    </div>
  )
}
