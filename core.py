import sys
from modules import shared

__version__ = "1.0.0"

# TODO: Add support for pause/resume control signals

class BrakeLight:
    '''
    A modular control interface for managing interrupt and skip behavior in AUTOMATIC1111 workflows.

    This class centralizes user-driven control signals such as interrupt and skip, providing consistent
    messaging to both the UI and console. It is designed to be workflow-agnostic, allowing reuse across
    batch scripts, extensions, and interactive tools.

    Core Features:
    - interrupt( phase ):          Halts execution if an interrupt flag is set, with contextual messaging.
    - skip( phase, message=None ): Returns True if a skip flag is set, allowing conditional bypass.
    - interrupt_or_skip(phase):    Combines interrupt and skip checks for streamlined control flow.
    - status( message ):           Updates UI and logs a status message.
    - reset():                     Clears both interrupt and skip flags.

    Usage:
        signals = ControlSignals()
        signals.reset()
        if signals.interrupt_or_skip( "image generation" ):
            return None
        signals.status( "Starting image generation..." )

    This class assumes that `shared.state.interrupted` and `shared.state.skipped` are available
    and mutable. It does not enforce behavior — it simply reports and responds to control flags.

    Designed for audit-friendly scripting environments.
    '''

    def __init__( self ):
        self.last_phase = None

    def _report_event( self, msg: str ):
        '''Unified status + console output for control events.'''
        shared.state.textinfo = msg
        print( msg )

    def interrupt_or_skip( self, phase_name ):
        self.interrupt( phase_name )
        return self.skip( phase_name )

    def interrupt( self, phase: str ):
        '''Hard stop if interrupt flag is set.'''
        self.last_phase = phase
        if shared.state.interrupted:
            self.status( f"🛑 Interrupt requested during {phase} — stopping" )
            shared.state.interrupted = False
            sys.exit( 0 )

    def skip( self, phase: str, message: str = None) -> bool:
        '''Returns True if skip was requested; clears the flag.'''
        self.last_phase = phase
        if getattr( shared.state, "skipped", False ):
            self.status( message or f"⏭️ Skip requested during {phase}" )
            shared.state.skipped = False
            return True
        return False

    def reset( self ):
        '''Resets both flags.'''
        shared.state.interrupted = False
        shared.state.skipped = False

    def status( self, message: str ):
        '''Sets live UI status and logs to console.'''
        shared.state.textinfo = message
        print( message )

