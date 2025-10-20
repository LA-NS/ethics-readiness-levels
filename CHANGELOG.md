# Ethics Readiness Levels Tool - Changelog

## Version 0.1 (2025-10-20)

### 🎉 Initial Release

**Major Features:**
- Complete implementation of Ethics Readiness Levels assessment methodology
- Clean, professional web interface with ivory background and Arial typography
- One-click answer selection (no radio buttons + submit workflow)
- Real-time progress tracking and score calculation
- 129 comprehensive ethics questions across 4 assessment blocks:
  - Zero Case (foundational ethics questions)
  - GDPR Block (data privacy and legal compliance)
  - AI Block (artificial intelligence specific ethics)
  - LED Block (legal enforcement directive compliance)

**Technical Implementation:**
- Flask web application with SQLite database backend
- Completely local operation (no external dependencies)
- Responsive design working on all device sizes
- Hierarchical question logic with conditional branching
- Session-based assessment state management

**Academic Integration:**
- Based on research paper: "Ethics Readiness of Artificial Intelligence: A Practical Evaluation Method" (under review)
- Authors: Laurynas Adomaitis (RISE), Vincent Israel-Jost (CEA-Saclay/Larsim), Alexei Grinbaum (CEA-Saclay/Larsim)
- Implemented and hosted by RISE (Research Institutes of Sweden)
- Funded by AIOLIA project (EU Grant 101187937) and MultiRATE EU Horizon project (Grant 101073929)

**User Experience:**
- Professional academic presentation with proper crediting
- Intuitive assessment flow with immediate visual feedback
- Clean results display with score breakdown
- Modern UI/UX following best practices for assessment tools

### 🔧 Technical Details

**Dependencies:**
- Python 3.7+
- Flask 2.3.3+
- SQLite3
- jQuery 3.5.1 (CDN)
- Optional: matplotlib for score visualization graphs

**Deployment:**
- Runs on localhost:8080 to avoid AirPlay conflicts on macOS
- Virtual environment setup with minimal requirements
- Debug mode enabled for development

**Database:**
- SQLite database with comprehensive question hierarchy
- Score weighting system for accurate ethics readiness calculation
- Support for conditional question branching based on initial responses

---

## Planned for Version 0.2

- User feedback integration and improvements
- Enhanced reporting capabilities
- Additional question blocks based on research feedback
- Performance optimizations
- Extended documentation