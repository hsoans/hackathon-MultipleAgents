
from pydantic import BaseModel, Field
from typing import List, Optional

class ReportFinding(BaseModel):
    """Specific result found during the project execution."""
    summary: str = Field(..., description="Short narrative of what was achieved")
    reasoning: str = Field(..., description="The 'Why' behind this specific approach")
    files_involved: List[str] = Field(..., description="Files created or modified for this finding")

class ProjectRisk(BaseModel):
    """Critical risks identified during the hackathon."""
    risk_title: str
    severity: str = Field("Medium", description="Low, Medium, High")
    description: str = Field(..., description="Why this is a risk and how it might fail")

class ExecutiveReport(BaseModel):
    """The final 'Developer-Friendly' output for Agent 5."""
    summary_narrative: str = Field(..., description="High-level prose overview")
    findings: List[ReportFinding]
    recommended_actions: List[str] = Field(..., description="Next steps for the user")
    risks: List[ProjectRisk]