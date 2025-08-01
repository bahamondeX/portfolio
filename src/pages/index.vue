<template>
  <div class="portfolio-container">
    <!-- Animated Gradient Background -->
    <div class="gradient-bg"></div>

    <!-- macOS-style Dock -->
    <div class="dock glassmorphic-card">
      <div
        v-for="item in dockItems"
        :key="item.id"
        class="dock-item glassmorphic-interactive"
        @click="scrollToSection(item.section)"
        :title="item.title"
      >
        <Icon :icon="item.icon" class="text-xl text-[#64ffda]" />
      </div>
    </div>

    <!-- Social Media Dock -->
    <div class="social-dock">
      <a
        v-for="social in socialLinks"
        :key="social.name"
        :href="social.url"
        target="_blank"
        class="social-item glassmorphic-interactive"
        :title="social.name"
      >
        <Icon :icon="social.icon" class="text-lg text-[#64ffda]" />
      </a>
    </div>

    <!-- Hero Section -->
    <section id="hero" class="hero-section">
      <div class="hero-content">
        <h1 class="hero-name glow-text">{{ displayName }}</h1>
        <div class="hero-titles">
          <span class="typewriter glow-text">{{ currentTitle }}</span>
        </div>
        <div class="hero-scroll">
          <ChevronDown class="text-4xl text-[#64ffda] animate-bounce" />
        </div>
      </div>
      <!-- Parallax Background -->
      <div class="parallax-bg parallax-1" ref="parallax1"></div>
    </section>

    <!-- About Section -->
    <section id="about" class="section">
      <div class="container">
        <h2 class="section-title glow-text">About Me</h2>
        <div class="about-content glassmorphic-card p-8 rounded-lg">
          <p class="about-text">
            Passionate Full Stack Developer and Data Architect with extensive experience
            in building scalable AI-native applications and cloud infrastructure.
            Specialized in creating innovative solutions that bridge the gap between
            traditional software development and modern AI capabilities.
          </p>
        </div>
      </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="section">
      <div class="container">
        <h2 class="section-title glow-text">Skills</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8 mt-12">
          <Card
            v-for="skill in skills"
            :key="skill.name"
            class="glassmorphic-card hover:glassmorphic-interactive transition-all duration-300 transform hover:-translate-y-2 hover:shadow-xl group"
          >
            <CardContent class="flex flex-col items-center justify-center p-8">
              <Icon :icon="skill.icon" class="text-5xl text-[#64ffda] mb-4 group-hover:animate-pulse" />
              <CardTitle class="text-xl font-semibold text-white">{{ skill.name }}</CardTitle>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>

    <!-- Experience Section -->
    <section id="experience" class="section">
      <div class="container">
        <h2 class="section-title glow-text">Experience</h2>
        <div class="timeline">
          <div
            v-for="(job, index) in workHistory"
            :key="index"
            class="timeline-item"
            :class="{ 'timeline-item-right': index % 2 === 1 }"
          >
            <div class="timeline-content glassmorphic-card hover:glassmorphic-interactive">
              <div class="timeline-date">{{ formatDate(job.start) }} - {{ formatDate(job.end) }}</div>
              <h3 class="timeline-title">{{ job.title }}</h3>
              <h4 class="timeline-company">{{ job.company }}</h4>
              <p class="timeline-description">{{ job.description }}</p>
            </div>
            <div class="timeline-dot"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Education Section -->
    <section id="education" class="section">
      <div class="container">
        <h2 class="section-title glow-text">Education</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mt-12">
          <Card
            v-for="edu in education"
            :key="edu.institution"
            class="glassmorphic-card hover:glassmorphic-interactive transition-all duration-300 transform hover:-translate-y-2 hover:shadow-xl"
          >
            <CardContent class="p-8">
              <CardTitle class="text-2xl font-bold text-white mb-2">{{ edu.degree }}</CardTitle>
              <CardDescription class="text-lg text-[#64ffda] mb-2">{{ edu.field }}</CardDescription>
              <p class="text-gray-300 mb-2">{{ edu.institution }}</p>
              <span class="text-sm text-gray-400" v-if="edu.start">
                {{ formatDate(edu.start) }} - {{ formatDate(edu.end) }}
              </span>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section">
      <div class="container">
        <h2 class="section-title glow-text">Projects</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 mt-12">
          <Card
            v-for="project in projects"
            :key="project.name"
            class="flip-card glassmorphic-card hover:glassmorphic-interactive"
            @click="openProject(project.url)"
          >
            <div class="flip-card-inner">
              <div class="flip-card-front flex flex-col items-center justify-center p-8">
                <Code  class="text-6xl text-[#64ffda] mb-4" />
                <CardTitle class="text-2xl font-semibold text-white">{{ project.name }}</CardTitle>
              </div>
              <div class="flip-card-back flex flex-col items-center justify-center p-8"
						:style="{ backgroundImage: `url(${project.image})`,
								backgroundSize: 'cover',
								backgroundPosition: 'center'
							}"
							>
                <CardTitle class="text-2xl font-semibold text-gray-500 mb-2">{{ project.name }}</CardTitle>
                <CardDescription class="text-gray-500 mb-4">Click to visit project</CardDescription>
                <ExternalLink  class="text-4xl text-red-500" />
              </div>
            </div>
          </Card>
        </div>
      </div>
      <!-- Parallax Background -->
      <div class="parallax-bg parallax-2" ref="parallax2"></div>
    </section>

    <!-- Accomplishments Section -->
    <section id="accomplishments" class="section">
      <div class="container">
        <h2 class="section-title glow-text">Accomplishments</h2>
        <div class="flex flex-col gap-6 mt-12">
          <div
            v-for="(accomplishment, index) in accomplishments"
            :key="index"
            class="accomplishment-item glassmorphic-card p-6 rounded-lg flex items-start gap-4"
          >
            <div class="accomplishment-icon flex-shrink-0">
              <LucideIcon name="Award" class="text-3xl text-[#64ffda]" />
            </div>
            <p class="accomplishment-text text-lg text-gray-300">{{ accomplishment }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
      <div class="container">
        <h2 class="section-title glow-text">Contact Me</h2>
        <div class="flex justify-center">
          <form @submit.prevent="submitForm" class="contact-form w-full max-w-lg glassmorphic-card p-8 rounded-lg">
            <div class="mb-6">
              <Label for="name" class="block text-lg font-medium text-gray-300 mb-2">Name</Label>
              <Input
                id="name"
                v-model="form.name"
                required
                class="glassmorphic-input w-full px-4 py-3 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-[#64ffda]/50"
              />
            </div>
            <div class="mb-6">
              <Label for="email" class="block text-lg font-medium text-gray-300 mb-2">Email</Label>
              <Input
                type="email"
                id="email"
                v-model="form.email"
                required
                class="glassmorphic-input w-full px-4 py-3 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-[#64ffda]/50"
              />
            </div>
            <div class="mb-6">
              <Label for="message" class="block text-lg font-medium text-gray-300 mb-2">Message</Label>
              <Textarea
                id="message"
                v-model="form.message"
                required
                rows="5"
                class="glassmorphic-input w-full px-4 py-3 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-[#64ffda]/50"
              ></Textarea>
            </div>
            <Button type="submit" class="submit-btn w-full py-3 rounded-md text-lg font-semibold flex items-center justify-center gap-2">
              <span>Send Message</span>
              <LucideIcon name="Send" class="text-xl" />
            </Button>
          </form>
        </div>
        <!-- Simple message box for form submission -->
        <div v-if="showMessage" class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-[1001]">
          <div class="glassmorphic-card p-8 rounded-lg text-center max-w-sm">
            <h3 class="text-2xl font-bold text-[#64ffda] mb-4">Message Sent!</h3>
            <p class="text-lg text-white mb-6">Thank you for your message! I'll get back to you soon.</p>
            <Button @click="showMessage = false" class="py-2 px-6 rounded-md text-lg font-semibold">
              Close
            </Button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { Icon } from '@iconify/vue'

// Lucide icon import
import { ChevronDown, Code, ExternalLink} from 'lucide-vue-next'

interface WorkHistory {
  company: string
  title: string
  start: string
  end: string
  description: string
}

interface Education {
  institution: string
  start?: string
  end?: string
  degree: string
  field: string
}

interface Project {
  name: string
  url: string
  image?: string
}

interface Skill {
  name: string
  icon: string // Lucide icon name
}

interface DockItem {
  id: string
  title: string
  icon: string // Lucide icon name
  section: string
}

interface SocialLink {
  name: string
  url: string
  icon: string // Lucide icon name
}

interface ContactForm {
  name: string
  email: string
  message: string
}

// Refs
const dock = ref<HTMLElement>()
const parallax1 = ref<HTMLElement>()
const parallax2 = ref<HTMLElement>()

// Reactive data
const displayName = ref('')
const currentTitle = ref('')
const currentTitleIndex = ref(0)
const form = reactive<ContactForm>({
  name: '',
  email: '',
  message: ''
})
const showMessage = ref(false) // For custom message box

// Data from the provided JSON (updated with Lucide icon names)
const workHistory: WorkHistory[] = [
  {
    company: "Globant",
    title: "Senior Data Engineer",
    start: "2023-09",
    end: "2024-12",
    description: "I developed Data Development Framework for internal side projects with automatic-onboarding (RAG enhanced Chatbot with Local LLM on Documentation Website). I developed OpenAI Replica with Open Source Models."
  },
  {
    company: "Pronti AI",
    title: "Backend Engineer",
    start: "2023-02",
    end: "2023-09",
    description: "Migrated a Flask MVP to a Production Kubernetes Cluster of FastAPI, Celery, RabbitMQ and Milvus for Image Embeddings processing for a fashion apparel."
  },
  {
    company: "Bluetab an IBM Company",
    title: "Data Developer",
    start: "2022-01",
    end: "2022-07",
    description: "Responsible for reporting the compliance of financial institutions to their HQs. Developed PCI compliant Spark Jobs with PySpark."
  },
  {
    company: "Indra",
    title: "Big Data Developer",
    start: "2021-03",
    end: "2021-12",
    description: "Developed data pipelines and automation workflows for financial institutions. Developed Datamart Framework on top of AWS RedShift, AWS Athena and AWS S3."
  },
  {
    company: "Telefónica",
    title: "Presales Engineer",
    start: "2017-07",
    end: "2020-10",
    description: "Design and development of Telco E2E proposals. Sizing of Cisco, Fortinet, Audiocodes solution components. Experience in Government B2B consulting sales and tender biddings."
  }
]

const education: Education[] = [
  {
    institution: "Pontificia Universidad Católica del Perú",
    start: "2006-12",
    end: "2012-12",
    degree: "Grado en ingeniería",
    field: "Ingeniería De Telecomunicaciones"
  },
  {
    institution: "Instituto Nacional de Investigación y Capacitación de Telecomunicaciones (INICTEL-UNI)",
    degree: "Diplomatura",
    field: "Diplomado En Gestión De Proyectos De Las Tic Bajo El Enfoque Pmi®"
  },
  {
    institution: "Colegio Pre-Universitario PAMER",
    start: "2004-03",
    end: "2006-12",
    degree: "High school",
    field: "School"
  }
]

const projects: Project[] = [
  {
    name: "Quipubase",
    url: "https://quipubase.oscarbahamonde.com",
	image: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png"
  },
  {
    name: "Lucidata",
    url: "https://lucidata.oscarbahamonde.com",
	image: "https://miro.medium.com/v2/resize:fit:804/format:webp/1*_wHSbu5vUwGkFtgWt6D_FQ.png"
  },
  {
    name: "Youtube Transcriber",
    url: "http://aai.oscarbahamonde.com",
	image: "/youtube_transcriber.png"
  },
  {
    name: "rustid",
    url: "https://github.com/bahamondex/rustid",
	image: "https://www.rust-lang.org/logos/rust-logo-512x512.png"
  },
  {
    name: "markdown_normalization",
    url: "https://github.com/bahamondex/markdown_normalization",
	image: "https://www.rust-lang.org/logos/rust-logo-512x512.png"
  },
  {
    name: "base64perf",
    url: "https://github.com/bahamondex/base64perf",
	image: "https://upload.wikimedia.org/wikipedia/commons/1/18/C_Programming_Language.svg"
  }
]

const accomplishments: string[] = [
  "While working at Telefónica Perú, I faced a significant challenge: the company was burdened by immense technical debt, with systems siloed by a legacy mainframe controlling billing. This made innovation nearly impossible, as departments operated in isolation, and crucial processes were managed through inefficient tools like email and Excel.",
  "I built Quipubase, Quipubase is a cutting-edge, real-time document database specifically engineered for the demands of AI-native applications. Key Features for Developers: High Performance: Built on RocksDB for efficient, high-throughput data operations.",
  "Winner of AWS UG Peru Hackathon 'AWS Cybersecurity Day'"
]

const skills: Skill[] = [
  { name: 'Python', icon: 'logos:python' },
	 { name: 'FastAPI', icon: 'logos:fastapi-icon' },
 { name: 'PyTorch', icon: 'logos:pytorch-icon' },
  { name: 'PostgreSQL', icon: 'logos:postgresql' },

  { name: 'AWS', icon: 'logos:aws' },
  { name: 'Google Cloud', icon: 'logos:google-cloud' },
  { name: 'Docker', icon: 'logos:docker-icon' },
 { name: 'Kubernetes', icon: 'logos:kubernetes' },
{ name: 'TypeScript', icon: 'logos:typescript-icon' },
  { name: 'Nuxt.js', icon: 'logos:nuxt-icon' },
  { name: 'Next.js', icon: 'logos:nextjs-icon' },
	
 { name: 'Node.js', icon: 'logos:nodejs-icon' }, // Correct Lucide name 
 
 
  

]

const titles = ['Full Stack Developer', 'Data Architect', 'Cloud Architect']

const dockItems: DockItem[] = [
  { id: 'home', title: 'Home', icon: 'mdi:home', section: 'hero' },
  { id: 'about', title: 'About', icon: 'mdi:user', section: 'about' },
  { id: 'skills', title: 'Skills', icon: 'mdi:code', section: 'skills' },
  { id: 'experience', title: 'Experience', icon: 'mdi:briefcase', section: 'experience' },
  { id: 'education', title: 'Education', icon: 'mdi:graduation-cap', section: 'education' },
  { id: 'projects', title: 'Projects', icon: 'mdi:folder-open', section: 'projects' },
  { id: 'contact', title: 'Contact', icon: 'mdi:mail', section: 'contact' }
]

const socialLinks: SocialLink[] = [
  { name: 'GitHub', url: 'https://github.com/bahamondex', icon: 'mdi:github' },
  { name: 'Twitter', url: 'https://x.com/ssc_obahamonde', icon: 'mdi:twitter' },
  { name: 'Website', url: 'https://oscarbahamonde.com', icon: 'mdi:globe' }
]

// Methods
const typeWriter = (text: string, element: any, speed: number = 100) => {
  return new Promise<void>((resolve) => {
    let i = 0
    const timer = setInterval(() => {
      if (i < text.length) {
        element.value += text.charAt(i)
        i++
      } else {
        clearInterval(timer)
        resolve()
      }
    }, speed)
  })
}

const animateTitle = async () => {
  while (true) {
    for (let i = 0; i < titles.length; i++) {
      currentTitle.value = ''
      await typeWriter(titles[i], currentTitle, 100)
      await new Promise(resolve => setTimeout(resolve, 2000))

      // Erase effect
      while (currentTitle.value.length > 0) {
        currentTitle.value = currentTitle.value.slice(0, -1)
        await new Promise(resolve => setTimeout(resolve, 50))
      }
    }
  }
}

const animateName = async () => {
  const name = 'Oscar Bahamonde'
  displayName.value = ''
  await typeWriter(name, displayName, 150)
}

const scrollToSection = (sectionId: string) => {
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}

const formatDate = (dateString: string) => {
  if (!dateString) return 'Present'
  const [year, month] = dateString.split('-')
  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  return `${months[parseInt(month) - 1]} ${year}`
}

const openProject = (url: string) => {
  window.open(url, '_blank')
}

const submitForm = () => {
  // Simulate form submission
  console.log('Form submitted:', form)
  showMessage.value = true // Show custom message box
  Object.assign(form, { name: '', email: '', message: '' })
}

// Parallax effect
const handleScroll = () => {
  const scrolled = window.pageYOffset
  if (parallax1.value) {
    parallax1.value.style.transform = `translate3d(0, ${scrolled * 0.5}px, 0)`
  }
  if (parallax2.value) {
    parallax2.value.style.transform = `translate3d(0, ${scrolled * 0.3}px, 0)`
  }
}

onMounted(() => {
  animateName()
  setTimeout(() => {
    animateTitle()
  }, 2000)

  window.addEventListener('scroll', handleScroll)

  // Animate elements on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-in')
      }
    })
  }, observerOptions)

  document.querySelectorAll('.section').forEach(section => {
    observer.observe(section)
  })
})
</script>

<style scoped>
/* Base styles and fonts */
.portfolio-container {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: #0a0a0a; /* Dark background for contrast */
  color: #ffffff;
  overflow-x: hidden;
  scroll-behavior: smooth;
}

/* Animated Gradient Background */
.gradient-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(-45deg, #0a0a0a, #1a1a2e, #16213e, #0f3460);
  background-size: 400% 400%;
  animation: gradientShift 15s ease infinite;
  z-index: -2;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Glowing Text */
.glow-text {
  text-shadow: 0 0 10px #64ffda, 0 0 20px #64ffda, 0 0 30px #64ffda;
  animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
  from { text-shadow: 0 0 10px #64ffda, 0 0 20px #64ffda, 0 0 30px #64ffda; }
  to { text-shadow: 0 0 20px #64ffda, 0 0 30px #64ffda, 0 0 40px #64ffda; }
}

/* Glassmorphism Utility Classes */
.glassmorphic-card {
  background: rgba(255, 255, 255, 0.08); /* Slightly less transparent */
  backdrop-filter: blur(25px); /* Stronger blur */
  border: 1px solid rgba(255, 255, 255, 0.15); /* More visible border */
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2); /* Subtle shadow */
  border-radius: 15px; /* Consistent rounded corners */
}

.glassmorphic-interactive {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease-in-out;
}

.glassmorphic-interactive:hover {
  background: rgba(100, 255, 218, 0.15); /* Highlight color */
  border-color: rgba(100, 255, 218, 0.4);
  box-shadow: 0 10px 40px rgba(100, 255, 218, 0.3);
  transform: translateY(-5px); /* Subtle lift on hover */
}

.glassmorphic-input {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #ffffff;
  transition: all 0.3s ease;
}

.glassmorphic-input:focus {
  background: rgba(100, 255, 218, 0.05);
  border-color: #64ffda;
  box-shadow: 0 0 0 2px rgba(100, 255, 218, 0.3);
}

/* macOS Dock */
.dock {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  padding: 10px;
  gap: 10px;
  z-index: 1000;
  border-radius: 20px;
}

.dock-item {
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dock-item:hover {
  transform: translateY(-10px) scale(1.2);
  box-shadow: 0 10px 30px rgba(100, 255, 218, 0.3);
}

/* Social Media Dock */
.social-dock {
  position: fixed;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  gap: 15px;
  z-index: 1000;
}

.social-item {
  width: 45px;
  height: 45px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: #64ffda;
  text-decoration: none;
  font-size: 18px;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.2);
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
}

.social-item:hover {
  transform: scale(1.2);
  background: rgba(100, 255, 218, 0.2);
  box-shadow: 0 0 20px rgba(100, 255, 218, 0.4);
}

/* Hero Section */
.hero-section {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.hero-content {
  text-align: center;
  z-index: 10;
}

.hero-name {
  font-size: 4rem;
  font-weight: 700;
  margin-bottom: 1rem;
  opacity: 0;
  animation: fadeInUp 1s ease 0.5s forwards;
}

.hero-titles {
  font-size: 2rem;
  font-weight: 300;
  margin-bottom: 2rem;
  height: 3rem; /* Fixed height to prevent layout shift */
}

.typewriter {
  border-right: 2px solid #64ffda;
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 50% { border-color: #64ffda; }
  51%, 100% { border-color: transparent; }
}

.hero-scroll {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 2rem;
  color: #64ffda;
}

.animate-bounce {
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%, 20%, 53%, 80%, 100% { transform: translateY(0); }
  40%, 43% { transform: translateY(-10px); }
  70% { transform: translateY(-5px); }
}

/* Parallax Backgrounds */
.parallax-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 120%;
  height: 120%;
  background-size: cover;
  background-position: center;
  z-index: -1;
}

.parallax-1 {
  background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)),
              url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><rect fill="%23001122" width="1200" height="800"/><circle cx="300" cy="200" r="100" fill="%23003366" opacity="0.3"/><circle cx="900" cy="600" r="150" fill="%23004488" opacity="0.2"/></svg>');
}

.parallax-2 {
  background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)),
              url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><rect fill="%23112233" width="1200" height="800"/><polygon points="600,100 700,300 500,300" fill="%23224466" opacity="0.4"/><polygon points="200,400 400,500 100,600" fill="%23336699" opacity="0.3"/></svg>');
}

/* Sections */
.section {
  padding: 100px 0;
  position: relative;
  opacity: 0;
  transform: translateY(50px);
  transition: all 0.8s ease;
}

.section.animate-in {
  opacity: 1;
  transform: translateY(0);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-title {
  font-size: 3rem;
  text-align: center;
  margin-bottom: 4rem;
  font-weight: 700;
}

/* About Section */
.about-content {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.about-text {
  font-size: 1.2rem;
  line-height: 1.8;
  color: #ccc;
}

/* Skills Grid (handled by Tailwind classes on Card component) */

/* Timeline */
.timeline {
  position: relative;
  max-width: 1000px;
  margin: 0 auto;
}

.timeline::after {
  content: '';
  position: absolute;
  width: 2px;
  background: linear-gradient(to bottom, #64ffda, #4a9eff);
  top: 0;
  bottom: 0;
  left: 50%;
  margin-left: -1px;
}

.timeline-item {
  padding: 10px 40px;
  position: relative;
  background-color: inherit;
  width: 50%;
}

.timeline-item-right {
  left: 50%;
}

.timeline-item::after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  right: -10px;
  background: #64ffda;
  border-radius: 50%;
  top: 15px;
  box-shadow: 0 0 20px rgba(100, 255, 218, 0.6);
  z-index: 1; /* Ensure dot is above line */
}

.timeline-item-right::after {
  left: -10px;
}

.timeline-content {
  padding: 2rem;
  position: relative;
  transition: all 0.3s ease;
}

.timeline-date {
  color: #64ffda;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.timeline-title {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: #fff;
}

.timeline-company {
  color: #4a9eff;
  margin-bottom: 1rem;
}

.timeline-description {
  color: #ccc;
  line-height: 1.6;
}

/* Education Grid (handled by Tailwind classes on Card component) */

/* Projects Section */
.flip-card {
  perspective: 1000px; /* For 3D flip effect */
  height: 250px; /* Fixed height for consistent cards */
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden; /* Safari */
  backface-visibility: hidden;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  box-sizing: border-box;
}

.flip-card-front {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
}

.flip-card-back {
  background: rgba(100, 255, 218, 0.15);
  border: 1px solid rgba(100, 255, 218, 0.4);
  box-shadow: 0 8px 32px 0 rgba(100, 255, 218, 0.3);
  transform: rotateY(180deg);
  cursor: pointer;
}

.project-icon {
  font-size: 4rem;
  color: #64ffda;
  margin-bottom: 1rem;
}

.project-link-icon {
  font-size: 2.5rem;
  color: #4a9eff;
}

/* Accomplishments Section */
.accomplishment-item {
  /* Styling handled by glassmorphic-card and flex utilities */
}

.accomplishment-icon {
  color: #64ffda;
}

.accomplishment-text {
  /* Styling handled by Tailwind text classes */
}

/* Contact Section */
.contact-form {
  /* Styling handled by glassmorphic-card and Tailwind utilities */
}

.submit-btn {
  background: linear-gradient(45deg, #64ffda, #4a9eff);
  color: #0a0a0a;
  font-weight: 700;
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
  box-shadow: 0 5px 15px rgba(100, 255, 218, 0.4);
}

.submit-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(100, 255, 218, 0.6);
  opacity: 0.9;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .dock {
    width: 90%;
    padding: 8px;
    gap: 8px;
  }
  .dock-item {
    width: 40px;
    height: 40px;
    font-size: 18px;
  }
  .social-dock {
    right: 10px;
    gap: 10px;
  }
  .social-item {
    width: 40px;
    height: 40px;
    font-size: 16px;
  }
  .hero-name {
    font-size: 3rem;
  }
  .hero-titles {
    font-size: 1.5rem;
    height: 2.5rem;
  }
  .section-title {
    font-size: 2.5rem;
    margin-bottom: 3rem;
  }
  .about-text {
    font-size: 1rem;
  }
  .timeline::after {
    left: 20px; /* Move timeline line to left for mobile */
  }
  .timeline-item {
    width: 100%;
    padding-left: 60px; /* Space for dot */
    padding-right: 10px;
  }
  .timeline-item::after, .timeline-item-right::after {
    left: 10px; /* Align dot with line */
  }
  .timeline-item-right {
    left: 0%; /* Align right items to left */
  }
  .education-grid, .projects-grid {
    grid-template-columns: 1fr;
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
