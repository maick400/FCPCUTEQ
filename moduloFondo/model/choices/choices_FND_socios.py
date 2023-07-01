GENEROS_CHOICES = (
        ('MAS', 'Masculino'),
        ('FEM', 'FEmenino'),
        ('ND', 'No definido'),
        )

ESTADOS_CIVILES_CHOICES = (
        ('SOL', 'Soltero/a'), 
        ('CAS', 'Casado/a'), 
        ('DIV', 'Divorciado/a'), 
        ('VIU', 'Viudo/a'), 
        ('ULB', 'Unión libre'),
        )


TIPO_PRESTACION_CHOICES = (
        ('QUI', 'Quirografario'),
        ('PRE', 'Prendario'),
    )


ESTADO_CHOICES = (
        ('A', 'ACTIVO'),
        ('I', 'INACTIVO'),
    )


PAIS_CHOICES = (
        ('ECU', 'Ecuador'),
        ('COL', 'Colombia'),
        ('PER', 'Perú'),
        ('BOL', 'Bolivia'),
        ('CHI', 'Chile'),
        ('ARG', 'Argentina'),
        ('BRA', 'Brasil'),
        ('URU', 'Uruguay'),
        ('PAR', 'Paraguay'),
        ('VEN', 'Venezuela'),
        ('PAN', 'Panamá'),
        ('COS', 'Costa Rica'),
        ('NIC', 'Nicaragua'),
        ('HON', 'Honduras'),
        ('SAL', 'El Salvador'),
        ('GUA', 'Guatemala'),
        ('MEX', 'México'),
        ('USA', 'Estados Unidos'),
        ('CAN', 'Canadá'),
        ('ESP', 'España'),
        ('POR', 'Portugal'),
        ('FRA', 'Francia'),
        ('ITA', 'Italia'),
        ('ALE', 'Alemania'),
        ('ING', 'Inglaterra')
        )

TIPO_IDENTIFICACION_CHOICES = (
        ('CED', 'Cédula'),
        ('PAS', 'Pasaporte'),
        ('RUC', 'RUC'),
        ('OTR', 'Otro'),        
        )

TIPO_SISTEMA_CHOICES = (
        ('CAP', 'Capitalización'),
        ('RENT', 'Renta'),
        ('MIX', 'Mixto'),
        )

BASE_CALCULO_APORTACION_CHOICES = (
        ('SUEL', 'Sueldo'),
        ('BAS', 'Básico'),
        ('OTR', 'Otro'),
        )

TIPO_RELACION_CHOICES = (
        ('CON', 'Conyugue'),
        ('HIJ', 'Hijo/a'),
        ('PAD', 'Padre'),
        ('MAD', 'Madre'),
        ('HER', 'Hermano/a'),
        ('TIO', 'Tío/a'),
        ('PRI', 'Primo/a'),
        ('SUE', 'Suegro/a'),
)

ESTADO_DE_REGISTRO_CHOICES = (
        ('A', 'ACTIVO'),
        ('I', 'INACTIVO'),
        ('E', 'ELIMINADO'),
        )